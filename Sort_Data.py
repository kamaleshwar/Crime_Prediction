import os
import csv
import datetime
import shutil

date = datetime.datetime.now()

source = 'Normalized_Data'

months = ['January', 'February','March','April','May','June','July','August','September','October','November','December']

block = {}
block_tmp = {}

months_year ={}

test= ""

target_dir = 'Sorted_data_set'

fr = open('Weather_details.csv',"rb")
reader = csv.reader(fr)

for row in reader:
    if row[1] == "harsh":
        if(months_year.has_key(row[0].split(" ")[0]+":"+row[0].split(" ")[2])):
            months_year[row[0].split(" ")[0]+":"+row[0].split(" ")[2]] = months_year[row[0].split(" ")[0]+":"+row[0].split(" ")[2]] + 1
        else:
            months_year[row[0].split(" ")[0]+":"+row[0].split(" ")[2]] = 1

for each in months_year.keys():
    if(months_year[each]>=16):
        months_year[each] = "harsh"
    else:
        months_year[each] = "normal"

def Sort_Data():
    global test
    if(not os.path.isdir(source)):
        print "Directory Doesn't Exist"
    else:
        files = os.listdir(source)
    for file in files:
        block = {}
        fr = open(source+"\\"+file,"rb")
        file_reader = csv.reader(fr)
        for row in file_reader:
            key = row[0]+":"+row[1]
            block[key] = row

        key_val = ""

        for year in range(2013,2016):
            for month in months:
                check = date.strftime("%B")+":"+date.strftime("%Y")
                key_val = month+":"+str(year)
                if(check == key_val):
                    break
                next = (months.index(month)+1)%12
                next_mon_key = months[next]+":"+str(year)
                if(not block.has_key(key_val)):
                    if(block.has_key(next_mon_key)):
                        miss_list = [month,year,'0','N/A',months_year[key_val],'0','0','0',block[next_mon_key][2]]
                    else:
                        miss_list = [month,year,'0','N/A',months_year[key_val],'0','0','0','0']
                    block_tmp[key_val] = miss_list
                else:
                    if(block.has_key(next_mon_key)):
                        add_list= block[key_val]
                        add_list.append(block[next_mon_key][2])
                        block_tmp[key_val] = add_list
                    else:
                        add_list= block[key_val]
                        add_list.append('0')
                        block_tmp[key_val] = add_list

            if(check == key_val):
                break
        write_to_File(block_tmp,file)

def write_to_File(info_map,file_name):
    global target_dir
    if(not os.path.isdir(target_dir)):
        os.mkdir(target_dir)

    fw = open(target_dir+"\\"+file_name,"ab")
    wr = csv.writer(fw)

    for row in info_map.values():
        wr.writerow(row)

def old_data():
    global source
    shutil.rmtree(source)


print "Sorting data..."
Sort_Data()
old_data()

print "Sorting Completed"
