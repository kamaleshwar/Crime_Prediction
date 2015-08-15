from __future__ import division
import csv
import os
import Create_blocks
import shutil

files = []
target_dir = "Normalized_Data"
source = "Blocks"
path_sep = os.path.sep

Theft_max = {}
Theft_min = {}
Robbery_max = {}
Robbery_min = {}
Burglary_max = {}
Burglary_min = {}
Arrest_max = {}
Arrest_min = {}


def get_max_min():
    global files
    if(not os.path.isdir(source)):
        print "Directory Doesn't Exist"
    else:
        files = os.listdir(source)

    for each_file in files:
        fr = open(source+path_sep+each_file,"rb")
        file_reader = csv.reader(fr)
        num_theft_max = 0
        num_theft_min = 0
        num_burglary_max=0
        num_burglary_min=0
        num_robbery_max=0
        num_robbery_min=0
        num_arrest_max = 0
        num_arrest_min = 0

        for max_min_row in file_reader:
            if(num_theft_max < int(max_min_row[3])):
                num_theft_max = int(max_min_row[3])
            if(num_theft_min > int(max_min_row[3])):
                num_theft_min = int(max_min_row[3])

            if(num_burglary_max < int(max_min_row[6])):
                num_burglary_max = int(max_min_row[6])
            if(num_burglary_min > int(max_min_row[6])):
                num_burglary_min = int(max_min_row[6])

            if(num_robbery_max < int(max_min_row[7])):
                num_robbery_max = int(max_min_row[7])
            if(num_robbery_min > int(max_min_row[7])):
                num_robbery_min = int(max_min_row[7])

            if(num_arrest_max < int(max_min_row[8])):
                num_arrest_max = int(max_min_row[8])
            if(num_arrest_min > int(max_min_row[8])):
                num_arrest_min = int(max_min_row[8])


        Theft_max[each_file.split(".")[0]] = num_theft_max
        Theft_min[each_file.split(".")[0]] = num_theft_min
        Burglary_max[each_file.split(".")[0]] = num_burglary_max
        Burglary_min[each_file.split(".")[0]] = num_burglary_min
        Robbery_max[each_file.split(".")[0]] = num_robbery_max
        Robbery_min[each_file.split(".")[0]] = num_robbery_min
        Arrest_max[each_file.split(".")[0]] = num_arrest_max
        Arrest_min[each_file.split(".")[0]] = num_arrest_min


def Normalize():
    global files
    if(not os.path.isdir(source)):
        print "Directory Doesn't Exist"
    else:
        files = os.listdir(source)

    for each_file in files:
        fr = open(source+path_sep+each_file,"rb")
        file_reader = csv.reader(fr)
        for row in file_reader:
            one_row = []
            one_row.append(row[0])
            one_row.append(row[1])
            if((Theft_max[each_file.split(".")[0]]-Theft_min[each_file.split(".")[0]])>0):
                one_row.append((int(row[3]) - int(Theft_min[each_file.split(".")[0]]))/(Theft_max[each_file.split(".")[0]]-Theft_min[each_file.split(".")[0]]))
            else:
                one_row.append((int(row[3])))
            one_row.append(row[4])
            one_row.append(row[5])

            if((Burglary_max[each_file.split(".")[0]]-Burglary_min[each_file.split(".")[0]])>0):
                one_row.append((int(row[6]) - int(Burglary_min[each_file.split(".")[0]]))/(Burglary_max[each_file.split(".")[0]]-Burglary_min[each_file.split(".")[0]]))
            else:
                one_row.append((int(row[6])))

            if((Robbery_max[each_file.split(".")[0]]-Robbery_min[each_file.split(".")[0]])>0):
                one_row.append((int(row[7]) - int(Robbery_min[each_file.split(".")[0]]))/(Robbery_max[each_file.split(".")[0]]-Robbery_min[each_file.split(".")[0]]))
            else:
                one_row.append((int(row[7])))

            if((Arrest_max[each_file.split(".")[0]]-Arrest_min[each_file.split(".")[0]])>0):
                one_row.append((int(row[8]) - int(Arrest_min[each_file.split(".")[0]]))/(Arrest_max[each_file.split(".")[0]]-Arrest_min[each_file.split(".")[0]]))
            else:
                one_row.append((int(row[8])))

            fw = open(target_dir+path_sep+each_file,"ab")
            file_writer = csv.writer(fw)
            file_writer.writerow(one_row)

        fr.close()
    shutil.rmtree(source)


def main():
    get_max_min()
    print "max min data prepared"
    if(not os.path.isdir(target_dir)):
        os.mkdir(target_dir)
    print "Normalizing data..."
    Normalize()
    print "Normalized"

if __name__ == '__main__':
  main()


