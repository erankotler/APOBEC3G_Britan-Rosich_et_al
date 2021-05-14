import os
import sys


def downsample(in_dir, out_dir, n_reads):
	downsampler_path="/users/ekotler/projects/A3G/Code/sample_fastq.py" # a python2 script that downsamples a fastq file

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


if __name__ == "__main__":

	### For experiment #1:
	# in_dir = "/mnt/lab_data/kundaje/users/ekotler/A3G/Data/downsampled_572/in"
	# out_dir = "/mnt/lab_data/kundaje/users/ekotler/A3G/Data/downsampled_572"
	# n_reads = 1500000

	### For experiment #2:
	#in_dir = "/mnt/lab_data/kundaje/users/ekotler/A3G/Data/downsampled_exp2/in"
	#out_dir = "/mnt/lab_data/kundaje/users/ekotler/A3G/Data/downsampled_exp2"
	#n_reads = 300000

	### For experiment #3:
	# in_dir = "/mnt/lab_data/kundaje/users/ekotler/A3G/Data/downsampled_651_20210102/in"
	# out_dir = "/mnt/lab_data/kundaje/users/ekotler/A3G/Data/downsampled_651_20210102"
	# n_reads = 1500000

	### For experiment #4:
	# in_dir = "/mnt/lab_data/kundaje/users/ekotler/A3G/Data/downsampled_665_20210124/in"
	# out_dir = "/mnt/lab_data/kundaje/users/ekotler/A3G/Data/downsampled_665_20210124"
	# n_reads = 100000

        ### For experiment #5
	in_dir = "/mnt/lab_data/kundaje/users/ekotler/A3G/Data/downsampled_kotler_run684_20210225/in"
	out_dir = "/mnt/lab_data/kundaje/users/ekotler/A3G/Data/downsampled_kotler_run684_20210225"
	n_reads = 1500000


	downsample(in_dir, out_dir, n_reads)
