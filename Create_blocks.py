import csv
import os

fr = open('Original_2013_temp.csv',"rb")
reader = csv.reader(fr)

def Create_blocks():
    global reader
    global THEFT_Max
    global THEFT_Min
    blocks = {}
    mon_year = {}
    Titles = ['Date' , 'Year','Block','Theft_Count','Location','Weather','Robbery_Count','Burglary_Count','Arrest_Count']

    for row in reader:
        if(row[3]=="THEFT" or row[3]=="ROBBERY" or row[3]=="BURGLARY"):
            if(row[3]=="THEFT"):
                row[3] = 1
                if(not mon_year.has_key(row[0]+":"+row[1]+"$"+row[2])):
                    row.append(0)
                    row.append(0)
                    row.append(0)
                    mon_year[row[0]+":"+row[1]+"$"+row[2]] = row
                else:
                    mon_year[row[0]+":"+row[1]+"$"+row[2]][3] = mon_year[row[0]+":"+row[1]+"$"+row[2]][3]+1

            elif(row[3]=="ROBBERY"):
                row[3] = 0
                if(not mon_year.has_key(row[0]+":"+row[1]+"$"+row[2])):
                    row.append(1)
                    row.append(0)
                    row.append(0)
                    mon_year[row[0]+":"+row[1]+"$"+row[2]] = row
                else:
                    mon_year[row[0]+":"+row[1]+"$"+row[2]][7] = mon_year[row[0]+":"+row[1]+"$"+row[2]][7]+1

            elif(row[3]=="BURGLARY"):
                row[3] = 0
                if(not mon_year.has_key(row[0]+":"+row[1]+"$"+row[2])):
                    row.append(0)
                    row.append(1)
                    row.append(0)
                    mon_year[row[0]+":"+row[1]+"$"+row[2]] = row
                else:
                    mon_year[row[0]+":"+row[1]+"$"+row[2]][8] = mon_year[row[0]+":"+row[1]+"$"+row[2]][8]+1

            if(row[4]=="TRUE"):
                row[3] = 0
                if(not mon_year.has_key(row[0]+":"+row[1]+"$"+row[2])):
                    row.append(0)
                    row.append(0)
                    row.append(1)
                    mon_year[row[0]+":"+row[1]+"$"+row[2]] = row
                else:
                    mon_year[row[0]+":"+row[1]+"$"+row[2]][9] = mon_year[row[0]+":"+row[1]+"$"+row[2]][9]+1

    print "Gathering Data"

    for each_block_mon_year in mon_year.keys():
        details = each_block_mon_year.split("$")
        ind = len(details)-1
        if(not blocks.has_key(details[ind])):
            blocks[details[ind]] = []
            mon_year[each_block_mon_year].pop(4)
            blocks[details[ind]].append(mon_year[each_block_mon_year])
        else:
            mon_year[each_block_mon_year].pop(4)
            blocks[details[ind]].append(mon_year[each_block_mon_year])

    print "Creating block files..."

    target_dir="Blocks"

    if(not os.path.isdir(target_dir)):
        os.mkdir(target_dir)

    path_sep = os.path.sep

    for each_block in blocks.keys():
        fw = open(target_dir+path_sep+each_block+".csv","ab")
        write = csv.writer(fw)
        #write.writerow(Titles)
        max_theft = 0
        min_theft = 0
        for each_block_det in blocks[each_block]:
            write.writerow(each_block_det)
            if max_theft < int(each_block_det[3]):
                max_theft = int(each_block_det[3])

    fr.close()
    fw.close()

def main():
    Create_blocks()
    print "Blocks created"
if __name__ == '__main__':
  main()



