import os

#Rey Cabral

directoryName = "Documents" #Directory to be searched
parentDirectory = "/Users/reycabralr/"  #absolute path to the parent directory of the directory to be searched.
extension = ".TXT"  # File extension to find


def findFiles(directoryName, extension):
    files = []
    for file in os.listdir(os.path.join(parentDirectory, directoryName)):
        if file.endswith(extension.lower()):
            files.append(file)
    return(files)

for file in findFiles(directoryName,extension):
    print(file)

