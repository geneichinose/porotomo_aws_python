#!/Users/ichinose1/miniconda3/bin/python3

### /home/ichinose1/python/bin/python3

import sys
import numpy
from obspy              import read
from obspy.core         import UTCDateTime
from obspy.io.segy.core import _read_segy
from obspy.io.sac       import SACTrace

class coords:
	def __init__( self, x, y, id ):
		self.x = x
		self.y = y
		self.id = id

######
###### start program
######
nargs = int(len(sys.argv)) - 1
args  = str(sys.argv)

if nargs != 2 :
	print( "error need 1 args got %d " % nargs )
	print( "text files: segy_filename rec_filename" )
	sys.exit()

segy_filename = str( sys.argv[1] )
rec_filename  = str( sys.argv[2] )

## read the SEG-Y file
##
st = _read_segy( segy_filename )
print( "segy_filename = " + segy_filename + " number of traces = %d " % len(st) )

list = []
with open( 'fiber.sgy.ll.xy', 'r' ) as file1:
	for line in file1:
		vector = line.split()
		list.append( coords( vector[0], vector[1], vector[2] ) )
	file1.close()

receivers = []
with open( rec_filename, 'r' ) as file2:
	for line in file2:
		receivers.append(line.rstrip('\n'))
	file2.close()

for irec in receivers:
	i = int( irec );
	
	for obj in list :
		if obj.id == str(i) :
			stla = obj.y
			stlo = obj.x
			staname = "D" + str(obj.id).zfill(4)
			# print( staname, stla, stlo )
			break

	tr = st[i]
	start_date_string = tr.stats.starttime.strftime("%Y.%j.%H.%M.%S.%f")
	sacfilename = start_date_string + '.' + str(i).zfill(4) + '.sac'
	print( "sacfilename = " + sacfilename )
	header = { 'kstnm': staname, 'knetwk': 'DAS', 'kcmpnm': 'BHZ', 'stla': stla, 'stlo': stlo, 'user0': i }
	sac = SACTrace( data=tr.data, **header )
	sac.delta = tr.stats.delta
	sac.b = tr.stats.starttime
	sac.reftime = tr.stats.starttime
	sac.write( sacfilename )
