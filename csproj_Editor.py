import ast
import datetime
import glob
import sys

print ('Version: {}{}{} {}'.format(sys.version_info[0], sys.version_info[1], sys.version_info[2], sys.version_info[3]))

datum1 = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
print (f'Start date: {datum1}')

filelist = glob.glob('c://Repositories//Sorter_SHP1' + '//**//*.csproj', recursive=True)
previousposition = 0
substring1 = '    <TargetFrameworkVersion>v4.0'
substring2 = '    <TargetFrameworkVersion>v4.6.1'

for filename in filelist :
    with open(filename, 'r+') as fileobj :
        line = fileobj.readline()
        while line:
            currentposition = fileobj.tell()            
            if substring1 in line :
                newline = line.replace(substring1, substring2)
                fileobj.seek(previousposition)
                fileobj.writelines(newline)
                print(f'file was modified: {filename}')
                break
            previousposition = currentposition
            line = fileobj.readline()

datum2 = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
print ('End date: {}'.format(datum2))
