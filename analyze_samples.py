import pandas as pd
import os
import argparse
import numpy as np
from Bio import Seq, SeqIO
import time
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from A3G_seq_analysis_helper import *



def parse_args():
	parser = argparse.ArgumentParser(description="Extract peak regions from bigwig file to produce a lighter bigiwg for quick visualization on browser. PROVIDE ABSOLUTE PATHS!")
	parser.add_argument("--experiment", type=str, required=True, help="Name of experiment (e.g. 'experiment 1')")
	# parser.add_argument("--data_d", type=str, required=True, help="Input (raw) data dir containig fastq files for analysis")
	parser.add_argument("--output_d", type=str, required=True, help="Path for saving results")

	args = parser.parse_args()		
	print(args)
	return(args)


def get_params():
	params = {}
	
	# Seqs and params:
	params["read_len"] = 150 # Read length in seq run
	params["fwd_primer"] = "GCCTCTGCTAACCATGTTCATGCC"

	# Entire correct (reference) amplicon seq:
	params["corr_seq"] = "GCCTCTGCTAACCATGTTCATGCCTTCTTCTTTTTCCTACAGCTCCTGGGCAACGTGCTGGTTATTGTGCTGTCTCATCATTTTGGCAAAGAATTCTAGGGATAACAGGGTAATGGATCCACCGGTCGCCACCATGGTGAGCAAGGGCGAGGAGCTGTTCACCGGGGTGGTGCCCATCCTGG"
	params["rest_site"] = "TAGGGATAACAGGGTAAT" # Note: restriction site runs from 96 to 114 (in extracted seqs, should fall at bp 77)
	# cleavage_site = "GATAACAGGG" # cleavage site itself 

	# Usable sequence query definition:
	params["seq_start_query"] = params["fwd_primer"][-5:] # query to look for to define relevant seqs
	params["expected_start_pos"] = 19 # expected position for the search query


	# alignment penalties:
	params["algnmt_params"] = {"match": 2,
					 "mismatch": -1,
					 "gap_open": -0.5,
					 "gap_extend": 0}

	# reference sequnce from plasmid for alignment:
	params["reference"] = params["corr_seq"][params["expected_start_pos"]:params["read_len"]] 
	return (params)


def perform_downsampling(experiment_name):
	""" Downsample fastq files in a given experiment to equal depth. 
	Defines paths to raw fastq files and downsampled outputs, and requested read depth (defined by lowest sample in experiment).
	Returns path to daownsampled data
	"""
	base_d = "/mnt/lab_data/kundaje/users/ekotler/A3G/Data/Britan-Rosich" # Base path to data

	if experiment_name=="experiment_1": ## Run572
		in_dir = os.path.join(base_d, "run572") 
		n_reads = 1500000

	elif experiment_name=="experiment_2": # Run609
		in_dir = os.path.join(base_d, "run609") 	
		n_reads = 300000

	elif experiment_name=="experiment_3": ## Run651
		in_dir = os.path.join(base_d, "run651") 	
		n_reads = 1500000

	elif experiment_name=="experiment_4": ## Run 665
		in_dir = os.path.join(base_d, "run665") 	
		n_reads = 100000

	else:
		print ("Unrecognized experiment name")

	out_dir = os.path.join(in_dir, "downsampled")
	if not os.path.isdir(out_dir):
		os.mkdir(out_dir)

	downsample(in_dir, out_dir, n_reads) # Perform downsampling 
	print ("Downsampling complete, saved to", out_dir)
	return (out_dir)


def analyze_all_samples(args, params):
	data_d = args.downsampled_data_d
	results_d = args.output_d
	if not os.path.isdir(results_d):
		os.mkdir(results_d)

	fs = [f for f in os.listdir(data_d) if f.endswith(".fastq")]
	for f in fs:
		print("Analyzing sample %s"%f)
		base_name = f.split("_")[0]
		cnts_f = os.path.join(results_d, base_name+"_counts.csv")
		algn_f = os.path.join(results_d, base_name+"_alignments.csv")
		
		analyze_samp(fastq_f=os.path.join(data_d, f), 
				 seq_start_query=params["seq_start_query"], 
				 expected_start_pos=params["expected_start_pos"], 
				 cleavage_site = params["rest_site"],
				 reference_seq=params["reference"], 
				 algnmt_params=params["algnmt_params"],
				 cnts_f=cnts_f, 
				 algn_f=algn_f,
				 nrows=None)
		
	print("DONE, files saved to", results_d)


def main():
	args = parse_args()
	params = get_params()

	# Downsample files:
	args.downsampled_data_d = perform_downsampling(args.experiment)
	
	# Analyze:
	analyze_all_samples(args, params)




if __name__ == "__main__":
	main()



