import csv
import os

fr = open('Weather_details.csv',"rb")
reader = csv.reader(fr)

if os.path.isfile('Original_2013_temp.csv'):
    os.remove('Original_2013_temp.csv')

fw = open('Original_2013_temp.csv',"ab")

write = csv.writer(fw)
fd = open('Original_2013.csv',"rb")
read = csv.reader(fd)

final = {}
months_year ={}

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

for each in read:
    if(read.line_num ==1):
        each.append("Weather")
        write.writerow(each)
    else:
        each.append(months_year[each[0]+":"+each[1]])
        write.writerow(each)

print "Created file with weather details"

fw.close()
fr.close()
fd.close()


