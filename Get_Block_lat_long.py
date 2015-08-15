from geopy.geocoders import Nominatim
import os
import csv

Geocoder =  Nominatim()
fr = open('Street_Names.csv')
read = csv.reader(fr)
fw = open('Block_lat_long.csv','ab')
write = csv.writer(fw)

print "Preparing Block map files..."

for row in read:
    each = []
    try:
        results = Geocoder.geocode(str(row[0])+" CHICAGO")
        each = [row[0],results.latitude,results.longitude]
        write.writerow(each)
    except Exception:
        continue

print "Block map files completed"

fw.close()
fr.close()




