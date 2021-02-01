import math
def fun(a,b,c): 
    determinant = (b**2) - (4*a*c)
    if determinant == 0:
        solution = (-1*b)/2*a
        print(f"The equation has equal roots and it is: {solution}")
    elif determinant > 0:
        determinant = math.sqrt(determinant)
        solution1 = ((-1*b) + determinant)/2*a
        solution2 = ((-1*b) - determinant)/2*a
        print(f"The equation has 2 distinct roots and they are {solution1} and {solution2}")
    else:
        print("The equation has no real roots")


fcoeff = float(input("Enter the coefficient of x^2: "))
scoeff = float(input("Enter the coefficient of x: "))
cons = float(input("Enter the constant value: "))


fun(fcoeff,scoeff,cons)



