def print_underscores():
    print("-------------")

def print_lots_of_equal_signs():
    print("===============")

print("This is line 1")
print_underscores()
print("This is line 2")
print_underscores()
print("This is line 3")
print_lots_of_equal_signs()


def print_separator(width):
    for x in range(width):
        print_lots_of_equal_signs("x", end="")
        print()


def print_separator_2(width):
    print_lots_of_equal_signs("x" * width)






def hello_world(name):
    print ("Hello" + name)
#Use hello_world to print a greeting
hello_world("Brandon")



# Define a function with 2 parameters
def add_numbers(numer1, number2, number3):
    print("Adding 3 numbers")
    print(int(numer1) + int(number2) + int(number3))

add_numbers(1, 2, 3)
def add_numbers(numer1, number2):
    print("Adding 2 numbers")
    print(int(numer1) + int(number2))

print("Adding 1 + 2 gives")
add_numbers(1, 2)

#Passing parameters to a function
def print_value(value):
    print (value)
my_variable1 = "Brandon"
my_variable2 = "Wood"
this_is_a_space = " "

print_value(my_variable1 + this_is_a_space + my_variable2)


#fuction return

def add_numbers(num1, num2):
    result = int(num1) + int(num2)
    return result
my_result = add_numbers(1, 2)
print(my_result)



def is_number_negative (n):
    if n < 0:
        return True
    return False
the_number = input("Please enter a number :")


if is_number_negative(int(the_number)):
    print("Negative")
else:
    print("Positive")


def is_number_negative(n):
    if n < 0:
        print("Negative")
    else:
        print("Positive")
the_number = input("Please enter a number :")


is_number_negative(int(the_number))

















