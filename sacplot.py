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

print(str(st))
st.plot( outfile="plot.nofilter.png", show=False )

st.filter( "bandpass", freqmin=0.1, freqmax=2.0, corners=2, zerophase=True  )
st.plot( outfile="plot.filter_2hz.png", show=False )
