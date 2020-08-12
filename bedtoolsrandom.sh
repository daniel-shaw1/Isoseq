###generate (-n)number random regions of size (-l) from genome size file. 

#PBS -S /bin/bash
#PBS -q batch
#PBS -N job_bt
#PBS -l nodes=1:ppn=6
#PBS -l walltime=48:00:00
#PBS -l mem=10gb

cd $PBS_O_WORKDIR
module load BEDTools/2.26.0-foss-2016b
bedtools random -l 200 -n 10000 -g chrom.sizes
