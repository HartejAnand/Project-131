import csv

rows=[]
with open("brown_dwarfs.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        rows.append(row)

