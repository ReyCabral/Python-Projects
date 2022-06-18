import os

parentDirectory = "/Users/reycabralr/"  #absolute path to the parent directory of the directory to be searched.


def findFiles(directoryName, extension, startingFileName):
    files = []
    for file in os.listdir(os.path.join(parentDirectory, directoryName)):
        if file.endswith(extension.lower()) and file.lower().startswith(startingFileName.lower()):
            files.append(file)
    return(files)


print("Enter the name of the directory to search:")
directoryName = input()
print("Enter the type of files you want to search for, by indicating the file extension to use:")
extension = input()
print("Enter the starting few character of the file name:")
startingFileName = input()

findFiles = findFiles(directoryName,extension,startingFileName)
fileName = "fileNames.txt"
pathFile = os.path.join(parentDirectory, directoryName, fileName)

for file in findFiles:
    File = open(pathFile, "a")
    File.write(file)
    File.write("\n")
    File.close()
    
print(len(findFiles), " files found. The list of file names retrieved can be found in fileNames.txt file:",pathFile)
