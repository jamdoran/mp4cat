import glob, os
from natsort import natsorted
from time import sleep

#Define the ffmpeg commands to be executed 
# Note:  Will force overwrite (-y) if the files already exist
joinCommand     = r'ffmpeg -y -f concat -safe 0 -i list.txt -c copy NoAudioMovie.mp4'
addAudioCommand = r'ffmpeg -y -i NoAudioMovie.mp4 -i music.mp4 -c copy -map 0:v -map 1:a NewMovie.mp4'



# Grab the files from the local folder and use the natsort module
# To sort them naturally 1,2,3,...,9,10 etc. and not 1,10,2
# Use os.path.basename to strip the path from glob.glob 
files = natsorted([os.path.basename(x) for x in glob.glob('*.mp4')])

#Open a file, append the 'file' prefix and add the filename
#ffmpeg consumes this file and concatenates in this order
with open(r'./list.txt' , 'w') as fp:
    for file in files:
        if file in ['music.mp4', 'NewMovie.mp4','NoAudioMovie.mp4'] : 
            print ('Found Music Track or files from previous run - skipping')
            continue
        print (file)
        fp.write(f"file '{file}'\n")

# Using dumb shell, but fine for this purpose
print()
print()
os.system('cat list.txt')
print()
print('Will join files in the order above...')
print()
sleep(3)

# Run the join command to create one file with no audio
os.system(joinCommand)
print()
print()

# Add the music track
if os.path.isfile('./music.mp4'):
    print('Found Music track (music.mp4')
    print('Adding audio to new video...')
    print()
    sleep(3)
    os.system(addAudioCommand)
else:
    print ('No Audio Track Found')


# Remove NoAudio.mp4 video file
print()
print()
print('Deleting temporary files..')
os.remove('./NoAudioMovie.mp4')
print()


print('All Done!!')
print()

