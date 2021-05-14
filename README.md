# APOBEC3G_Britan-Rosich_et_al

This repository contains scripts used for the processing and analysis of sequencing data in the manuscipt "APOBEC3G protects the genome from radiation-induced damage" by Btiran-Rosich et. al. See manuscript for details about the analysis and for deposited data locations.
The analysis workflow consists of:
1) Downsampling fastq files from each experiment to an equal sequencing depth to enable unbiased comparions between samples.
2) Comparing sequencing reads in fastq files to the reference plasmid sequnce. This is performed by:
  2.1) Extract relevant reads from fastq (contatining relevant part of Fwd primer seq)
  2.2) Assess fraction of correctly repaired clevage sites (exact matches to reference) - examining the 18bp SceI cleavage site or the entire 131bp amplicon
  2.3) To facilitate XXXXX



Data organization:<br>

<path_to_base_dir$ tree <br>
.
├── run572 <br>
│   ├── MK1_S1_R1_001.fastq <br>
│   └── MK2_S2_R1_001.fastq <br>
├── run609 <br>
│   ├── MK10_S646_R1_001.fastq 
│   └── MK9_S645_R1_001.fastq 
├── run651
│   ├── MK13_S1_R1_001.fastq 
│   └── MK14_S2_R1_001.fastq 
└── run665
    ├── MK15_S14_R1_001.fastq
    ├── MK16_S15_R1_001.fastq
    ├── MK17_S16_R1_001.fastq
    └── MK18_S17_R1_001.fastq

