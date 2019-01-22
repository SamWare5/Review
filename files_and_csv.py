import csv

row_counter = 1
#unique_types = {}
unique_types = set()
europe_orders = 0
total_units_sold = 0

with open('7_-_100_Sales_Records.csv') as csv_file:

    reader = csv.reader(csv_file)
    for row in reader:

        if row_counter !=1:
            #unique_types[row[2]] = row[2]
            unique_types.add(row[2])
            total_units_sold += int(row[8])

            if row[0] == "Europe":
                europe_orders += 1

        row_counter += 1

print("Total amount of units sold {0}".format(total_units_sold))
print("Total records from Europe {0}".format(europe_orders))
print("")
print("Here is a list of unique ")

list_counter = 1
for x in unique_types:
    print(str(list_counter) + " " + x)
    list_counter += 1

