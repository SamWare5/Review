mylist2 = ["champlain", "dawson", "vanier"]
for college in mylist2:
    print(college.title())


import random
randomList = []
# Add random numbers to my list
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
print()
#print("The minimum value is " , minimum, " and the maximum value is ", maximum)

maxVal = randomList[0]
minVal = randomList[0]
total = 0
length = 0

for y in randomList:
    if y > maxVal:
        maxVal = y
#    print("maxVal = ", maxVal)

    if y < minVal:
        minVal = y

#    print("minVal = ", minVal)
    total = total + y
    length += 1
average = total/length
print("the final max value is", maxVal, "and the final min value is", minVal, "The total is", total, "the average is", average, "and The length is", length)

#print("the sum of the list is ", sum(randomList))















