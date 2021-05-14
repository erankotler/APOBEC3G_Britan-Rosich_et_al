#!/bin/bash
#
# Wrapper for analyzing all samples used in the manuscript by Britan-Rosich et al.
#

BASE_D=/mnt/lab_data/kundaje/users/ekotler/A3G/Data/Britan-Rosich # Base data dir (in which raw data subdirectories should be found)
RESULTS_D=$BASE_D/Results

for NUM in 1 2 3 4
do
	EXP_NAME=experiment_$NUM
	echo Analyzing $EXP_NAME...

	mkdir -p $RESULTS_D/$EXP_NAME

	python analyze_samples.py \
		--experiment $EXP_NAME \
		--output_d $RESULTS_D/$EXP_NAME

	echo Done

done