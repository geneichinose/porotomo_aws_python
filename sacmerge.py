#!/Users/ichinose1/miniconda3/bin/python3

import sys
import numpy
from obspy              import read
from obspy.core         import UTCDateTime
from obspy.io.sac       import SACTrace

######
###### start program
######
nargs = int(len(sys.argv))
progname = str(sys.argv[0]) 

### read the first SAC file, to initalize the Obspy.Stream
###
sacfilename0 = str( sys.argv[1] )
st = read( sacfilename0, format='SAC')

### read the rest of the SAC files and append 
###
for a in sys.argv[2:nargs]:
	sacfilename = str(a)
	st += read( sacfilename, format='SAC')

print( progname + " : merging : " )
print(str(st))
st.merge( method=0, fill_value=0, interpolation_samples=0 )
sacfilename0 = sacfilename0 + ".merged"
print( progname + " : writting SAC file=" + sacfilename0 )
st.write( sacfilename0, format='SAC' )
