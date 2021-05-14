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
	pass

	# base_d = "/mnt/lab_data/kundaje/users/ekotler/A3G/Data/Britan-Rosich" # Base path to data

	# ### For experiment #1 (Run572)
	# in_dir = os.path.join(base_d, "run572") 
	# n_reads = 1500000

	# ### For experiment #2 (Run609)
	# in_dir = os.path.join(base_d, "run609") 	
	# n_reads = 300000

	# ### For experiment #3 (Run651)
	# in_dir = os.path.join(base_d, "run651") 	
	# n_reads = 1500000

	# ### For experiment #4 (Run 665)
	# in_dir = os.path.join(base_d, "run665") 	
	# n_reads = 100000
	
	# out_dir = os.path.join(in_dir, "downsampled")

	# downsample(in_dir, out_dir, n_reads)
