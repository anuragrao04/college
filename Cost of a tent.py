import math
def cost(h, r, c, t):

    area_cylinder = 2*3.14*r*h

    l = math.sqrt((r*r) + (h*h))

    area_conical = 3.14*r*l
    print("Required area of canvas is: "+str(area_cylinder+area_conical)+" m^2")
    total_cost = (area_cylinder+area_conical) * c * 0.01 * t

    return total_cost



height = float(input("Enter height of the tent in metres: "))
radius = float(input("Enter area of the tent in metres: "))
cost_per_unit = float(input("Enter cost of canvas per metre: "))
tax = float(input("Enter GST: "))
 

print("required cost will be: "+ str(cost(height, radius, cost_per_unit, tax))+" rupees")



    
