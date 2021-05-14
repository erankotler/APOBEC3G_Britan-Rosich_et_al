#!/bin/bash
#
# Wrapper for analyzing all samples used in the manuscript by Britan-Rosich et al.
# See README for details
#
# Usage: 
# 	source analyze_all_exps <path_to_base_dir>


BASE_D=$1 # Base data dir (in which raw data subdirectories should be found)
# /mnt/lab_data/kundaje/users/ekotler/A3G/Data/Britan-Rosich 
RESULTS_D=$BASE_D/Results

for NUM in 1 2 3 4
	do
		EXP_NAME=experiment_$NUM
		echo Analyzing $EXP_NAME...

		mkdir -p $RESULTS_D/$EXP_NAME

		python analyze_samples.py \
			--experiment $EXP_NAME \
			--output_d $RESULTS_D/$EXP_NAME \
			| tee $RESULTS_D/$EXP_NAME/summary.txt

		echo Done

	done
echo "Analysis complete"