import pandas as pd
import os
import numpy as np
from Bio import Seq, SeqIO
# import gzip
import time
from Bio import pairwise2
from Bio.pairwise2 import format_alignment



def downsample(in_dir, out_dir, n_reads):
	''' Downsample fastq files in in_dir to a depth of n_reads, saved in out_d with same name '''
	
	downsampler_path="./sample_fastq.py" # a python2 script that downsamples a fastq file

	for f in os.listdir(in_dir):
		if f.endswith("fastq"):
			in_f = os.path.join(in_dir,f)
			out_f = os.path.join(out_dir,f)
			
			if out_f==in_f:
				out_f = "subsampled_"+out_f

			cmnd_s = "python2 %s -n %i %s %s"%(downsampler_path, n_reads, in_f, out_f)
			print (cmnd_s)
			os.system(cmnd_s)
			os.rename(out_f+".0", out_f)
		else:
			print("file %s is not a .fastq file (inputs should be unzipped fastq only) - skipping file"%f)



def extract_seqs(f, seq_start_query, expected_start_pos, read_len=150, nrows=None):
	"""Extract relevant reads from fastq which contain seq_start_query within 3 bp of expected_start_pos
	returns lists of Fwd reads that comply with the constraints and unmapped reads.
	"""
	tot_reads = 0
	fwds = []
	# revs = []
	unmapped = []
	with open(f, "rt") as h:
		for record in SeqIO.parse(h, "fastq"):
			tot_reads+=1
			s = str(record.seq)
			st_pos = s.find(seq_start_query) # look for end of Fwd primer around its expected location
			if st_pos>=expected_start_pos-3 and st_pos<=expected_start_pos+3: 
				fwds.append(s[st_pos:read_len])
	#         elif s.startswith(rev_primer[:6]):
	#             revs.append(s)
			else:
				unmapped.append(s)
			
			if nrows is not None and tot_reads>=nrows:
				break
				
	print ("Done extracting sequences (total reads in file: %i)"%tot_reads)    
	print ("%i reads of %i contain relevant fwd sequence (usable fraction=%f)"%(len(fwds), tot_reads, 
																			len(fwds)/tot_reads))
	return (fwds, unmapped)

def accurate_repair_stats(seqs, cleavage_site):
	"""Get fraction of correct (accurate) repairs (i.e. sequences in the list seqs with correct cleavge site)
	"""
	acc_fix = []
	inacc_fix = []
	for i in range(len(seqs)):
		pos = str(seqs[i]).find(cleavage_site)
		expected_pos = 77 # expected position for the search query (use 81 for central 10bp of site)
		if pos>=expected_pos-3 and pos<=expected_pos+3:
			acc_fix.append(seqs[i])
	#         print(pos)
		else:
			inacc_fix.append(seqs[i])

	print ("Fraction of correct cleavage sites (%s): %.3f"%(cleavage_site, len(acc_fix)/(len(inacc_fix)+len(acc_fix))))
	print("(%i accurate restriction sequences, %i inaccurate sequences)"%(len(acc_fix), len(inacc_fix)))
	return (acc_fix, inacc_fix)


def make_counts_tbl(seqs, out_f=None):
	""" returns a df with counts (#occurances) for each sequence, sorted by prevalence
	"""
	df = pd.DataFrame(seqs, columns=["seq"])
	df["count"] = 1
	cnts = df.groupby("seq").count().sort_values(by="count", ascending=False)
	if out_f is not None:
		cnts.to_csv(out_f)
	return cnts


def make_alignment_table(counts_tbl, reference, algnmt_params, top_seqs=1000, out_f=None):
	""" align sequences in counts_tbl to the correct (reference) seq. 
	The first alignment is stored for each sequence in the top_seqs most prevalent sequences.
	algnmt_params is a dict with penalty scores for alignment.
	returns a df with counts for each sequence and its formatted alignment string
	"""

	c = counts_tbl.head(top_seqs).copy()
	c["alignments"] = c.apply(lambda x:pairwise2.align.globalms(reference, x.name, 
																algnmt_params["match"], algnmt_params["mismatch"], 
																algnmt_params["gap_open"], algnmt_params["gap_extend"]),1)
	for i in c.index:
		a = c.loc[i, "alignments"][0]
		c.loc[i, "alignment1"] = format_alignment(*a)
	c = c.drop("alignments",1)
	if out_f is not None:
		c.to_csv(out_f, index=False)
		
	return c


def analyze_samp(fastq_f, seq_start_query, expected_start_pos, cleavage_site, reference_seq, algnmt_params, cnts_f=None, algn_f=None, read_len=150, nrows=None):
	""" Analize sample:
	1. Extract relevant reads from fastq (contatining relevant part of Fwd primer seq)
	2. Assess fraction of correctly repaired clevage sites
	3. Examine most prevalent sequences - align to plasmid sequence around the restriction site
	Counts and Alignments (for top prevalent seqs) saved to cnts_f and algn_f (csv files)
	Returns (#accurate cleavge sites, #inaccurate sites)
	"""
	fwds, unmapped = extract_seqs(fastq_f, seq_start_query, expected_start_pos, read_len, nrows)
	acc_fix, inacc_fix = accurate_repair_stats(fwds, cleavage_site)

	cnts = make_counts_tbl(fwds, out_f=cnts_f)
	algn_tbl = make_alignment_table(cnts, reference_seq, algnmt_params, top_seqs=1000, out_f=algn_f)
	print("DONE\n")



	