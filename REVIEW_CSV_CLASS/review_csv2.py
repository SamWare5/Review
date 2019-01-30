import csv

inch = 2.54
lbs = 0.453592


with open('biostats.csv', 'rt') as csv_file:
    inputfile = csv.reader(csv_file)
    next(inputfile, None)
    
    for row in inputfile:






