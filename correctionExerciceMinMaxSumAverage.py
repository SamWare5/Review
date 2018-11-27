import random

my_list = []
for x in range(10):
        my_list.append(random.randint(1, 1000))
print(my_list)


print(my_list)
max_of_list = my_list[0]
min_of_list = my_list[0]
sum_of_list = 0
length_of_list = 0

for x in my_list:

    length_of_list += 1
    sum_of_list += x

    if x > max_of_list:
        max_of_list = x
    if x < min_of_list:
        min_of_list = x
print("Sum = " + str(sum_of_list))
print("Size = " + str(length_of_list))
print("Greatest " + str(max_of_list))
print("Lowest " + str(min_of_list))

average_of_list = sum_of_list / length_of_list
print("Average " + str(average_of_list))



