import os

workingDirectory = "/Users/reycabralr/Documents/text-files/"
extension = ".txt"
fileName = "mergedContent.txt"
pathFile = os.path.join(workingDirectory, fileName)


def findFiles(workingDirectory, extension):
    files = []
    for file in os.listdir(os.path.join(workingDirectory)):
        if file.endswith(extension.lower()):
            files.append(file)
    return(files)

with open(pathFile, 'w') as outfile:
  
    # Iterate through list
    for file in findFiles(workingDirectory,extension):
  
        # Open each file in read mode

        with open(os.path.join(workingDirectory,file)) as infile:
  
            # read the data from file1 and
            # file2 and write it in file3
            outfile.write(infile.read())
  
        # Add '\n' to enter data of file2
        # from next line
        outfile.write("\n")    

