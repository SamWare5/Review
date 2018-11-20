mylist2 = ["champlain", "dawson", "vanier"]
for college in mylist2:
    print(college.title())


import random
randomList = []
# Add andom numbers to my list
for x in range(10):
    ranNumber = random.randint(1, 100)
    randomList.append(ranNumber)

#Dsplay the list (method 1)
print(randomList)

#Display the list method 2
for x in randomList:
  print (x, end=" ")

#minimum = min(randomList)
#maximum = max(randomList)
#print()
#print("The minimum value is " , minimum, " and the maximum value is ", maximum)

  for y in randomList:
      if y > maxVal:
          maxVal = y
    print(maxVal)



