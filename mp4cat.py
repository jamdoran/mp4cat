import glob, os
from natsort import natsorted
from time import sleep

#Define the ffmpeg command to run 
command = r'ffmpeg -f concat -safe 0 -i list.txt -c copy NewMovie.mp4'

# Grab the files from the local folder and use the natsort module
# To sort them naturally 1,2,3,...,9,10 etc. and not 1,10,2
# Use os.path.basename to strip the path from glob.glob 
files = natsorted([os.path.basename(x) for x in glob.glob('*.mp4')])

#Open a file, append the 'file' prefix and add the filename
#ffmpeg consumes this file and concatenates in this order
with open(r'./list.txt' , 'w') as fp:
    for file in files:
        fp.write(f"file '{file}'\n")

# Dumb shell, but fine for this purpose
print()
print()
os.system('cat list.txt')
print()
print('Will join files in the order above...')
print()
sleep(3)
os.system(command)

print()
print()
print('All Done!!')
print()

