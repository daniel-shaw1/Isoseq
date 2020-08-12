##Take 10000 regions generated using bedtools random, exlude genic regions from Y maker annotations, and include only regions that map on stratum 1 in the alignment file, and create bed file with 10,000 regions of 200bp.


#PBS -S /bin/bash
#PBS -q batch
#PBS -N job_bt
#PBS -l nodes=1:ppn=6
#PBS -l walltime=48:00:00
#PBS -l mem=10gb

cd $PBS_O_WORKDIR
module load BEDTools/2.26.0-foss-2016b
bedtools shuffle -i Yrandom.bed -g chrom.sizes -excl Y.bed -incl str1include.bed
