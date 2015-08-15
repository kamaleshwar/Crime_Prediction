# Read the field descriptors for the database file
sf.fields
[("DeletionFlag", "C", 1, 0), ["AREA", "N", 18, 5],
["BKG_KEY", "C", 12, 0], ["POP1990", "N", 9, 0], ["POP90_SQMI", "N", 10, 1],
["HOUSEHOLDS", "N", 9, 0],
["MALES", "N", 9, 0], ["FEMALES", "N", 9, 0]]
# Read the 2nd and 3rd field values of the 4th database record
sf.records[3][1:3]
['060750601001', 4715]
