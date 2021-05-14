# APOBEC3G_Britan-Rosich_et_al

This repository contains scripts used for the processing and analysis of sequencing data in the manuscipt "APOBEC3G protects the genome from radiation-induced damage" by Btiran-Rosich et. al. See manuscript for details about the analysis and for deposited data locations.
The analysis workflow consists of:
1. Downsampling fastq files from each experiment to an equal sequencing depth to enable unbiased comparions between samples.
1. Comparing sequencing reads in fastq files to the reference plasmid sequnce. This is performed by:
  - Extracting relevant reads from fastq (contatining relevant part of Fwd primer sequence)
  - Assessing fraction of correctly repaired clevage sites (exact matches to reference) - examining the 18bp SceI cleavage site or the entire 131bp amplicon
  - Blast alignment of each sequence to the reference




Input data organization:
```
<path_to_base_dir>$ tree

  ├── run572 
  │   ├── MK1_S1_R1_001.fastq
  │   └── MK2_S2_R1_001.fastq
  ├── run609 
  │   ├── MK9_S645_R1_001.fastq 
  │   └── MK10_S646_R1_001.fastq  
  ├── run651
  │   ├── MK13_S1_R1_001.fastq 
  │   └── MK14_S2_R1_001.fastq 
  └── run665
      ├── MK15_S14_R1_001.fastq
      ├── MK16_S15_R1_001.fastq
      ├── MK17_S16_R1_001.fastq
      └── MK18_S17_R1_001.fastq

```
