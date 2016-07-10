#!/bin/bash -l
#SBATCH --nodes=1 
#SBATCH --partition=workq
#SBATCH --time=1:00:00
#SBATCH --export=NONE
#SBATCH --account=pawsey0001

module swap PrgEnv-cray/5.2.82 PrgEnv-gnu
module load python wgs/8.3
# export PATH and PERL5LIB if necessary
# export PATH=/path/to/the/installed/runCA:$PATH 
# export PERL5LIB=/path/to/the/Exporter-Tiny/List-MoreUtils/Statistics-Descriptive/perl/modules:$PERL5LIB

aprun -n 1 runCA -p ecoli-trim -d ecoli-trim -s ecoli-trim.spec ecoli-untrimmed.frg
