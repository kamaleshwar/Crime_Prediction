from openpyxl import Workbook
from openpyxl import load_workbook
import sys
import os
import shutil

source  ='result.xlsx'

workbook = load_workbook(source)
work_sheet = workbook.active
max_rows = work_sheet.get_highest_row()
if(not os.path.isdir('subset')):
    os.mkdir('subset')

files = os.listdir('Final_data_set')

for each in range(1,max_rows+1):
    shutil.copyfile('Final_data_set\\'+work_sheet['A'+str(each)].internal_value+".xlsx",'subset\\'+work_sheet['A'+str(each)].internal_value+".xlsx")





