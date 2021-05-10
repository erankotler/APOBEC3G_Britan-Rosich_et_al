# APOBEC3G_Britan-Rosich_et_al

This repository contains scripts used for the processing and analysis of sequencing data in the manuscipt "APOBEC3G protects the genome from radiation-induced damage" by Btiran-Rosich et. al. See manuscript for details about the analysis and for deposited data locations.
The analysis workflow consists of:
1) Downsampling fastq files from each experiment to an equal sequencing depth to enable unbiased comparions between samples.
2) Comparing sequencing reads in fastq files to the reference plasmid sequnce. This is performed by:
  2.1) Extract relevant reads from fastq (contatining relevant part of Fwd primer seq)
  2.2) Assess fraction of correctly repaired clevage sites (exact matches to reference) - examining the 18bp SceI cleavage site or the entire 131bp amplicon
  2.3) To facilitate XXXXX




