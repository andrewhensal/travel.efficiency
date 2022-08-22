import matplotlib.pyplot as plt
import numpy as np
print("#########################################")
print("#  Welcome to the Efficiency Calculator #")
print("#########################################")
print("In the efficincy calculator you can calculate the efficiency, in gallons per person,\n of a trip comparing air travel and car travel. \n")
print("Please choose the following information:")
print("1. Trip distance in miles:")
d=int(input())


print("2. Aircraft (Boeing 737-924) 179 passengers") 
#Aircraft is Boeing 737-924 and max capacity is 179 passengers (MPG:1.57)
print("3. Aircraft (Airbus A320neo) 194 passengers \n")
#Aircraft is Airbus A320neo and max capacity is 194 passengers (MPG:1.58)


choice = int(input("Enter your choice: \n"))

print("Please enter the number of passengers:")
p=int(input())
if choice == 2:
    airmpg=1.57
elif choice == 3:
    airmpg=1.58
gal = (airmpg*d)//p
gal = int(gal)

def efficiency(d,p,gal):
    if choice == 2:
        if p>179:
            print("The aircraft is not able to carry the number of passengers you entered \n")
    else:
            print("The aircraft is able to carry the number of passengers you entered")
            print("The fuel consumption of the aircraft is:",gal,"gallons per passenger \n")
    if choice == 3:
    
        if p>194:
            print("The aircraft is not able to carry the number of passengers you entered")
    else:
            print("The aircraft is able to carry the number of passengers you entered")
            print("The fuel consumption of the aircraft is:",gal,"gallons per passenger \n")

efficiency(d,p,gal)
print("##################################################")
print("#Next, enter your automobile MPG, for comparison.#")
print("##################################################")
print("In this section, the program will take the number of passengers from the aircraft, and divide it by 5 (Max Cap of a car) and find the number of cars needed to carry the passengers.")
print("Input MPG of your car:")
mpg=int(input())
if mpg > 5:
    carsneeded = (p//5)
    galperpersn = (d//mpg*carsneeded)//p
    galperpersn = int(galperpersn)
    print("The number of cars needed to carry the passengers is:",carsneeded)
    print("The fuel consumption per person is :",galperpersn,"gallons per person")
    
if gal < galperpersn:
    print("The aircraft is more efficient than the car")
else:
    print("The car is more efficient than the aircraft")




