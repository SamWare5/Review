for n in range (25):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
        if n % 3 == 0:
            print("Fizz")
            if n % 5 == 0:
                print("Buzz")
    print(n)


