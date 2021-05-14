#!/bin/bash
# BASE_D=/mnt/lab_data/kundaje/users/ekotler/A3G/Data/exp_6_kotler_run715_20210421_ISceI
# RAW_DATA_D=$BASE_D/raw
# DOWNSAMPLED_DATA_D=$BASE_D/downsampled

EXP_NAME=experiment_6
RESULTS_D=/users/ekotler/projects/A3G/Results/exp_6_kotler_run715_20210421_ISceI

python analyze_samples.py \
	--experiment $EXP_NAME \
	--output_d $RESULTS_D


