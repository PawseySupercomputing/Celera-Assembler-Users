# Celera-Assembler-Users

This is a patch file for Celera Assembler 8.3rc2 'runCA.pl' to run on a Cray system where a hybrid scheduling system, SLURM + ALPS, is in use.
Celera 8.3rc2 does not come with SLURM support and Brett Whitty has done some work adding SLURM options to it:

       https://github.com/brettwhitty/bw-ca-tools

However, that patch is suitable for native SLURM.
With hybrid SLURM + ALPS, there needs to be some more tweaks.
 
This patch is based on Brett Whitty's version and can be applied by

        patch runCA runCA_SLURM_ALPS_patch
where runCA is the original perl script from wgs.

If you have any questions, please email
	charlene.yang@pawsey.org.au

# Testing

The patch has been tested in the following environement:
- Magnus supercomputer, Pawsey Supercomputing Centre
- Cray XC40, PrgEnv-gnu/5.2.82, gcc/4.8.2, craype-haswell
- SLURM slurm/14.11.8-pawsey-3
- Celera wgs/8.3rc2
- Data is Escherichia_coli_K12_MG1655, using uncorrected PacBio reads, with CA8.2

Testing scripts are included. First, download the sample ecoli sequence data and prepare for the run
	
	./get_ecoli_test_data.sh
which will generate a file called ecoli-untrimed.frg for later use.

Then to run the trimming test, submit the following script by
        
        sbatch job_script_trim.slurm
where job_script_trim.slurm is
        
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

Lastly, the assembly test is submitted by 
	
	sbatch job_script_assembly.slurm
and the job script is

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

      	aprun -n 1 runCA -p ecoli-assembly -d ecoli-assembly -s ecoli-assembly.spec ecoli-untrimmed.frg

