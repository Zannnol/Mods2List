# Mods2List - A simple python script
# This script writes using Markdown in a plane text file a lise of
# the mods files and their version (if included in their file name)
#
# Author NolanZ
import os.path
import glob


# Getting the mods folder path and checking if it exists
folderPath = ""
while(os.path.isdir(folderPath) == False):
    folderPath = input("Mods folder path : \n")
    if os.path.isdir(folderPath) == False:
        print("Folder does not exists !")

# Getting all the mods files
modsFilesList = list(map(os.path.basename, glob.glob(folderPath + "/*")))

# Creating and writing in a file
with open(r'./mods-list.txt', 'w') as fp:
    for item in modsFilesList:
        # Remove the '.jar' extension
        size = len(item)
        item = item[:size - 4]
        
        fp.write("- %s\n" % item)
    print("Done writing !")
