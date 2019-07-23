'''
This is a script which scans through a directory, retreives all of the file names, opens each of them, iterates through cells and 
creates a list of all the names. The list is then written to a text file.
'''

import os, openpyxl

working_folder = 'S:\PROGRAMMES\Globe_2020\PSG_PGeogs\Data\Modified_USGS'

os.chdir(working_folder)

names = os.listdir(working_folder)


for file in names:
    if file[0] == '~':
        names.remove(file)

formation_list = []
count = 0
state_count = 0

for file in names:
    try:
        xl_file = openpyxl.load_workbook(file)
        file_name = file.split('.')
        state = file_name[0]
        sheet = xl_file.get_sheet_by_name("Correct Schema")
        #print "Reading " + str(state) + "..."
        state_count += 1

        for row in range(2, sheet.max_row + 1):
            cell = sheet.cell(row, column=2).value
            cell = str(cell)
            cell = cell.strip()
            count += 1
            formation_list.append(str(state) + " : " + cell)
            
    except Exception as e:
        print str(file) + " Exception: " + str(e)
        print "Reading " + str(file) + " failed!"
        continue
        
formation_list = set(formation_list)
formation_list = list(formation_list)
formation_list.sort()
#print formation_list
print type(formation_list)
print "Number of returned formations: " + str(len(formation_list))
print "Number of cells read: " + str(count)
print "Number of files read: " + str(state_count)
 

print('Writing results...')
resultFile = open('formations.txt', 'w')
for fm in formation_list:
    resultFile.write(str(fm) + "\n")
resultFile.close()
print('Done.')


