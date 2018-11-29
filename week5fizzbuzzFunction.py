def is_divisible(num, test_num):
    if num % 3 == 0:
        return True
    return False


for num in range(0, 21):
        print(str(num) + ":", end="")
        if is_divisible(num, 3) and is_divisible(num, 5):
            print("FizzBuzz")
        elif is_divisible(num, 3):
            print("Fizz")
        elif is_divisible(num, 5):
            print("Buzz")
        else:
            print()
