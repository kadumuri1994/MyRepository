

pathnameIn = "D:\InputFilepath"
filenameIn = "InputFileNameInInputPath.extension"
pathIn = pathnameIn + "/" + filenameIn

pathnameOut = "D:\OutputFilePath"
filenameOut = "OutputFilenameInOutputPath.extension"
pathOut = pathnameOut + "/" + filenameOut

fileIn = open(pathIn,'r')
fileOut = open(pathOut,'w')

list={"WordA","WordB"} #Lines you want to extract (from your file) which consists of any of the strings (in array)
for line in fileIn:
    if  any(s in line for s in list): 
        fileOut.writelines(line)
        fileOut.write("\n")
    else:
        pass

fileIn.close()
fileOut.close()
