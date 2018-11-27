province_list = {"QC": "Quebec", "ON": "Ontario"}
prov = input("Enter the province code > ")

if prov.upper() not in province_list:
    print("Sorry the province code is not valid ")
else:
    result = province_list[prov.upper()]

    print("The province is  {0}".format(result))

my_list = {"A" : "Brendon", "B" : "Joe", "C" : "Mary" , "C" : "Peter" }
print(my_list["C"])

countries = {'us': "USA", 'fr': "France", 'uk': "United Kingdom"}
for i in countries.items():
    print(i[1])
print("-------------------------------")

for a, b in countries.items():
    print(b)
print("-------------------------------")
for v in countries.values():
    print(v)
