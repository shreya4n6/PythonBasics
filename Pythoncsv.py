import csv

with open('Book1.csv', mode='r',  errors="ignore")as file:

    csvFile=csv.reader(file)

    for lines in csvFile:
        print(lines)