import glob, os
from natsort import natsorted
from tkinter import Tk
from tkinter import filedialog
from datetime import datetime



#Get the working folder via TK Dialog box
def getWorkingFolder():

    # Default to the users home folder
    default_folder = '.'

    #Open a Dialogue Box to select a folder
    window = Tk()
    window.withdraw()  # Hide the tk window
    rootFolder = filedialog.askdirectory(initialdir=default_folder)
    window.destroy()

    # Check we got something
    if not rootFolder:
        print('User Cancelled !')
        exit()

    # Make folder a full path
    rootFolder = os.path.join(rootFolder, '')

    print (f'Working in {rootFolder}')
    print ()
    print ()

    return rootFolder




# Grab the files from the local folder and use the natsort module
# To sort them naturally 1,2,3,...,9,10 etc. and not 1,10,2
# Use os.path.basename to strip the path from glob.glob 
def returnSortedVideoFileList(rootFolder):
    files = natsorted([os.path.basename(x) for x in glob.glob(rootFolder+'*.mp4')])
    return files


#Open a file, append the 'file' prefix and add the filename
#ffmpeg consumes this file and concatenates in this order
def writeListFile(rootFolder, files):

    catCommand       = f'cat "{rootFolder}list.txt"'

    with open(f'{rootFolder}list.txt' , 'w') as fp:
        for file in files:
            if file in ['music.mp4', 'NewMovie.mp4','NoAudioMovie.mp4'] : 
                print ('Found Music Track or files from previous run - skipping')
                continue
            print (f'Adding -> {file}')
            fp.write(f"file '{rootFolder+file}'\n")

    # Using dumb shell, but fine for this purpose
    print()
    print()
    os.system(catCommand)
    print()
    print('Will join files in the order above...')
    print()



# Run the join command to create one file with no audio
def joinFiles(rootFolder):

    joinCommand = f'ffmpeg -y -f concat -safe 0 -i "{rootFolder}list.txt" -c copy "{rootFolder}NoAudioMovie.mp4"'
    os.system(joinCommand)
    


# Add a music track to the video if one exists
# File must be names music.mp4
def addMusicTrack(rootFolder):

    addAudioCommand = f'ffmpeg -y -i "{rootFolder}NoAudioMovie.mp4" -i "{rootFolder}music.mp4" -c copy -map 0:v -map 1:a "{rootFolder}NewMovie.mp4"'
    musicTrack      = os.path.join(rootFolder,"music.mp4")

    if os.path.exists(musicTrack):
        print()
        print()
        print('Found Music track (music.mp4')
        print('Adding audio to new video...')
        print()
        print()
        os.system(addAudioCommand)
    else:
        print ()
        print ('No Audio Track Found')
        print ()



def deleteTempFiles(rootFolder):

    # Remove NoAudio.mp4 video file
    print()
    print()
    print('Deleting temporary files..')

    noAudioFile = os.path.join(rootFolder, "NoAudioMovie.mp4")
    listFile    = os.path.join(rootFolder, "list.txt")

    os.remove(noAudioFile)
    os.remove(listFile)



#Open the rootFolder when everything is done
def openRootFolder(rootFolder):
    cmd = f'open "{rootFolder}"'
    os.system(cmd)



def main():
    
    startTime   = datetime.now()

    rootFolder  = getWorkingFolder()
    files       = returnSortedVideoFileList(rootFolder)
    
    writeListFile(rootFolder, files)
    joinFiles(rootFolder)
    addMusicTrack(rootFolder)
    deleteTempFiles(rootFolder)
    
    print()


    print( f'Complete in {datetime.now() - startTime } seconds' )
    print()
    print('All Done!!')
    print()

    openRootFolder(rootFolder)
    


# Run main() as the main function
if __name__ == '__main__':
    main()


