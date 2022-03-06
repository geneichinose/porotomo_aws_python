# Porotomo dataset is openly available on AWS s3 cloud storage. 
# https://gdr.openei.org/submissions/980
#
# download and install the AWS CLI for free.  https://aws.amazon.com/cli/
# Or use your browser (this requires signup but is free for basic tier with credit card for ID verification).  https://portal.aws.amazon.com/
#
# For example, using the CLI these two commands list the directory and then copies one of the SEG-Y files (30sec segment) to your current directory.
#
# List contents of directory: 
# > aws s3 ls s3://nrel-pds-porotomo/DAS/SEG-Y/DASH/  --no-sign-request
#
# List SEG-Y files near the time of the 2016-03-21T07:37:10 earthquake
# > aws s3 ls s3://nrel-pds-porotomo/DAS/SEG-Y/DASH/20160321/PoroTomo_iDAS16043_1603210737 --no-sign-request
# 2020-11-21 02:03:01 1048616640 PoroTomo_iDAS16043_160321073721.sgy
# 2020-11-21 02:03:01 1048616640 PoroTomo_iDAS16043_160321073751.sgy
#
# > aws s3 ls s3://nrel-pds-porotomo/DAS/SEG-Y/DASH/20160321/PoroTomo_iDAS16043_1603210738 --no-sign-request
# 2020-11-21 02:03:16 1048616640 PoroTomo_iDAS16043_160321073821.sgy
# 2020-11-21 02:03:35 1048616640 PoroTomo_iDAS16043_160321073851.sgy
#
# Copy three SEG-Y files 
# > aws s3 cp s3://nrel-pds-porotomo/DAS/SEG-Y/DASH/20160321/PoroTomo_iDAS16043_160321073721.sgy . --no-sign-request
# > aws s3 cp s3://nrel-pds-porotomo/DAS/SEG-Y/DASH/20160321/PoroTomo_iDAS16043_160321073751.sgy . --no-sign-request
# > aws s3 cp s3://nrel-pds-porotomo/DAS/SEG-Y/DASH/20160321/PoroTomo_iDAS16043_160321073821.sgy . --no-sign-request
#
# Convert 30s segment SEG-Y to SAC for only select channels specified in receivers.txt 100-105 out of 51-8761
# > ./readsegy2.py PoroTomo_iDAS16043_160321073721.sgy receivers.txt
# > ./readsegy2.py PoroTomo_iDAS16043_160321073751.sgy receivers.txt
# > ./readsegy2.py PoroTomo_iDAS16043_160321073821.sgy receivers.txt
#
# Merge the 30s segment SAC files for 6 selected channels
# > ./sacmerge.py *.0100.sac
# > ./sacmerge.py *.0101.sac
# > ./sacmerge.py *.0102.sac
# > ./sacmerge.py *.0103.sac
# > ./sacmerge.py *.0104.sac
# > ./sacmerge.py *.0105.sac
#
# Plot waveforms raw and 0.1-2 Hz
# > ./sacplot.py *.merged
