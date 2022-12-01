import ast
import datetime
import glob
import sys

print ('Version: {}{}{} {}'.format(sys.version_info[0], sys.version_info[1], sys.version_info[2], sys.version_info[3]))

datum1 = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
print ('Start date: {}'.format(datum1))

filelist = glob.glob('c://Repositories//Sorter_SHP1' + '//**//AssemblyInfo.cs', recursive=True)
#filelist = glob.glob('d://Teszt' + '//**//AssemblyInfo.cs', recursive=True)
previousposition = 0
substring1 = 'AssemblyVersion'
substring2 = 'AssemblyFileVersion'

for filename in filelist :
    with open(filename, 'r+') as fileobj :
        adjustmentDone1 = False
        adjustmentDone2 = False
        line = fileobj.readline()
        while line:
            currentposition = fileobj.tell()
            if '//' in line :
                None    
            elif substring1 in line and not adjustmentDone1:
                lineparts = line.split('.')
                if len(lineparts) >= 4 and lineparts[2].isnumeric :                
                    version = int(lineparts[2])
                    newline = lineparts[0] + '.' + lineparts[1] + '.' + str(version + 1) + '.' + lineparts[3]
                    fileobj.seek(previousposition)
                    fileobj.writelines(newline)
                    adjustmentDone1 = True
                    print(f'file ({filename}) was modified in entry: {substring1} to {newline}')
                    continue
            elif substring2 in line and not adjustmentDone2 :
                lineparts = line.split('.')
                if len(lineparts) >= 4 and lineparts[2].isnumeric :                
                    version = int(lineparts[2])
                    newline = lineparts[0] + '.' + lineparts[1] + '.' + str(version + 1) + '.' + lineparts[3]
                    fileobj.seek(previousposition)
                    fileobj.writelines(newline)
                    adjustmentDone2 = True
                    print(f'file ({filename}) was modified in entry: {substring2} to {newline}')
                    continue
            previousposition = currentposition
            line = fileobj.readline()

datum2 = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
print ('End date: {}'.format(datum2))
