
class Biostats:
    def __init__(self, name, sex, age, height, weight):

        self.name = name
        self.sex = sex
        self.age = age
        self.height = height
        self.weight = weight

import csv
sum_age = 0
averrage_age = 0

with open('biostats.csv', 'rt') as my_csv_file:
    inputfile = csv.reader(my_csv_file)

    for row in inputfile:
        print (row)




sum_age += int(row[2])

print(sum_age)


