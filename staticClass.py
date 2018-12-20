class School:
    region = "Montreal"
    name = ""
school1 = School()
school1.name = "Champlain"
school2 = School()
school2.name = "Dawson"
School.region= "Montreal"

print("School name for School1 is: " + school1.name)
print("Region for all School1s is: " + School.region)
print("School name for School1 is: " + school1.name)

