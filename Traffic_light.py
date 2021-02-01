def traffic_light(c):
    c = c.lower()
    
    if c not in ["green","yellow","red"]:
        print("Invalid input, try again")
        return 3

    elif c == 'red':
        return 0

    elif c == 'yellow':
        return 1

    else:
        return 2


def light(n):
    if n == 0:
        print("STOP! Your life is precious")

    elif n == 1:
        print("please WAIT till the light is green")

    elif n == 2:
        print("GO! Thank you for being patient")
  
        



while True:
    color = input("Enter light: (green/yellow/red): ")
    light(traffic_light(color))
