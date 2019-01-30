import csv

count = 0
sum = 0
female = 0
male = 0


with open('biostats.csv', 'rt') as csv_file:
    inputfile = csv.reader(csv_file)
    next(inputfile, None)

    for row in inputfile:
        count += 1
        sum += int(row[2])
        average = sum / count

        if row [1] =="M":
            male +=1
        elif row[1] =="F":
            female+=1
print(sum)
print("The average age is ", average)
print(count)
print("Percentage of Male is ", male/count*100)
print("Percentage of Female is ", female/count*100)








