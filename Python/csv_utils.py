import csv

with open('quotes.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
#        print(row)
#        print ("----------------------")
#        print(row[0])
        print ("----------------------")
        print(row[0],row[1],row[2],)
