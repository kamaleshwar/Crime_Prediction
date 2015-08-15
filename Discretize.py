import os
import csv
import shutil
source_dir = 'Sorted_data_set'
target_dir = 'Discretized_data_set'

def Discretize():
    files = os.listdir(source_dir)
    for file in files:
        fr = open(source_dir+"\\"+file,"rb")
        read = csv.reader(fr)
        if not os.path.isdir(target_dir):
            os.mkdir(target_dir)
        fw = open(target_dir+"\\"+file,"ab")
        write = csv.writer(fw)
        for row in read:
            copy = []
            copy = row
            if(float(copy[2])>0.4):
                copy[2] = 'critical'
            else:
                copy[2] = 'non-critical'
            if(float(copy[5])>0.4):
                copy[5] = 'critical'
            else:
                copy[5] = 'non-critical'
            if(float(copy[6])>0.4):
                copy[6] = 'critical'
            else:
                copy[6] = 'non-critical'
            if(float(copy[7])>0.4):
                copy[7] = 'critical'
            else:
                copy[7] = 'non-critical'
            if(float(copy[8])>0.4):
                copy[8] = 'critical'
            else:
                copy[8] = 'non-critical'
            write.writerow(copy)
    fr.close()
    fw.close()


print "Discreting..."
Discretize()
shutil.rmtree(source_dir)

print "Discretization Completed."
