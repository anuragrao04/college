import math
def add(x,y):
    return x+y

def sub(x,y):
    return x-y 

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

def answer(ans):

    print(f"The answer is: {ans}")
    




while True:
    print('''\n\nSelect the required operation:\n
    1. Addition
    2. Subtraction
    3. Division
    4. Multiplication
    5. Square Root
    6. Exit
    ''')

    choice = (input("\nEnter your choice: "))
    
    
    if choice not in {'1','2','3','4','5','6'}:
        print("Invalid input, please try again")
        continue
    
    if choice == '6':
        break


    if choice == '5':

        num = float(input("\nEnter number: "))
        ans = math.sqrt(num)
        answer(ans)
        continue

    fnum = float(input("\nEnter first number: "))
    snum = float(input("\nEnter second number: "))


    if choice == '1':
        ans = add(fnum, snum)
        answer(ans)

    elif choice == '2':
        ans = sub(fnum, snum)
        answer(ans)

    elif choice == '3':
        if snum == 0:
            print("\nWe can not divide a number with 0. Please try again.\n\n")
            continue
        ans = div(fnum,snum)
        answer(ans)

    elif choice == '4':
        ans = mul(fnum, snum)
        answer(ans)
    
    

