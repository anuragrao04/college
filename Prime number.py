number = int(input("Enter the number: ")) #input
count = 0 #variable for counting how many times given number divides with i 



for i in range(1,10): #divides from 1 to 9
    if number % i == 0:
        count = count + 1     #every time it divides, count is increased by 1
            

if count <=2: #divides only 2 or less times i.e., with 1 and itself, it is a prime number
    print(f"{number} is a prime number")

else: #else it is not prime 
    print(f"{number} is not a prime number")