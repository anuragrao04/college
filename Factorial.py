while True:

    num = int(input("Enter the number to find factorial: "))
    factorial = 1

    if num < 0:
        print("We can not find the factorial of a negative number.")

    elif num == 0:
        print("The factorial of 0 is 1")

    else:
        for i in range(1, num+1):
            factorial = factorial * i

        print(f"The factorial of {num} is {factorial}")



