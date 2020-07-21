#PBS -S /bin/bash
#PBS -N j-blat
#PBS -l nodes=1:ppn=24
#PBS -q batch
#PBS -l walltime=24:00:00
#PBS -l mem=20gb

cd $PBS_O_WORKDIR

module load BLAT/3.5-foss-2016b

blat female.all.tissues.filtered.converted.fasta male.all.tissues.filtered.converted.fasta malevsfemalepool.psl
