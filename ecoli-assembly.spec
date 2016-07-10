##
## This script is from 
## 	https://github.com/brettwhitty/bw-ca-tools
## with a few tweaks.
##
#############################
##
## Test job spec for Celera Assembler 'runCA.pl' SLURM support patch.
## Brett Whitty <brett@gnomatix.com>
## 
## Grabbed from: 
##   http://wgs-assembler.sourceforge.net/wiki/index.php/Escherichia_coli_K12_MG1655,_using_uncorrected_PacBio_reads,_with_CA8.2
## 
## Original authors of these data are credited with all sequence data and pipeline settings.
## Please see URL above for more information.
##

useGrid               = 1
scriptOnGrid          = 1  ## default in runCA is 0, but seems to work; disable if you wish
frgCorrOnGrid	      = 1
ovlCorrOnGrid	      = 1
gridEngine            = SLURM

coresPerNode          = 24
memPerNode            = 64 #GB
walltimeLimit         = "01:00:00"

merSize               = 19
merThreshold          = 0
merDistinct           = 0.9995
merTotal              = 0.995

mbtThreads	      = 24
ovlStoreMemory	      = 61440 #MB
merOverlapperThreads  = 24
merylThreads          = 24
frgCorrThreads        = 24
batMemory             = 60 #GB
batThreads 	      = 24
merQCmemory           = 2048

doOBT                 = 0
doExtendClearRanges   = 0

unitigger             = bogart

ovlErrorRate          = 0.35  #  Compute overlaps up to 35% error
utgGraphErrorRate     = 0.35  #  Unitigs at 35% error
utgMergeErrorRate     = 0.35  #  Unitigs at 35% error
cnsErrorRate          = 0.35  #  Needed to allow ovlErrorRate=0.35
cgwErrorRate          = 0.35  #  Needed to allow ovlErrorRate=0.35

ovlConcurrency        = 24
cnsConcurrency        = 24

ovlThreads            = 24
ovlHashBits           = 22 #23
ovlHashBlockLength    = 30000000 #10000000
ovlRefBlockSize       = 2000000 #25000 #2000000 # 25000 requies 118 nodes

#frgCorrBatchSize      = 1000
ovlCorrBatchSize      = 1000
#cnsReduceUnitigs      = 0 0   #  Always use only uncontained reads for consensus
cnsReuseUnitigs       = 1     #  With no mates, no need to redo consensus

cnsMinFrags           = 1000
cnsPartitions         = 256

cnsMaxCoverage        = 10    #  Limit consensus calling to 10x
