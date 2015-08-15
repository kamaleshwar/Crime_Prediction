import os
import glob
import csv
import shutil
from xlsxwriter.workbook import Workbook

source_dir= 'Discretized_data_set'
target_dir= 'Final_data_set'
path_sep = os.path.sep

print "Converting files to required format..."

if (os.path.isdir("Final_data_set")):
    shutil.rmtree('Final_data_set')

files = os.listdir(source_dir)

for file in files:
    if(not os.path.isdir(target_dir)):
        os.mkdir(target_dir)
    workbook = Workbook( target_dir+path_sep+file.split(".")[0] + '.xlsx')
    worksheet = workbook.add_worksheet()
    with open(source_dir+path_sep+file, 'rb') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)
    workbook.close()
    f.close()

shutil.rmtree(source_dir)

print "Comversion Completed"

