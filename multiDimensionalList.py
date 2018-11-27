students = [[88, 89, 100], [98, 60, 77], [89, 98, 90], [12, 13, 14]]
#1st quiz 2nd student
print(students[1][0])

#what is the max value of the quizzes for student#2
print(max(students[1]))

#what is the average of quizzes for students

car_inspection = [[True, False, True],
                    [True, True, True],
                    [False, False, False],
                    [True, True, True]]
count = 0

for car in car_inspection:
    count += 1
    print("inspection for car number " + str(count))
    print("Inspector 1 : " + str(car[0]))
    print("Inspector 2 : " + str(car[1]))
    print("Inspector 3 : " + str(car[2]))
    print()

#copy a list

a = [22, 33]

b = a

#that means b will only point to a

print("List a")
print(a)

print("List b")
print(b)

a[1] = 66
print("List a")
print(a)

print("List b")
print(b)



