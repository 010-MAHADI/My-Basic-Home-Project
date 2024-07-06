'''
import cmath

a = float(input("Enter value of a :"))
b = float(input("Enter value of b :"))
c = float(input("Enter value of c :"))

# Calculate the discriminant
D = (b**2 - 4*a*c)
    
   # Find two solutions using the quadratic formula
if D > 0:
    root1 = (-b + cmath.sqrt(D)) / (2 * a)
    root2 = (-b - cmath.sqrt(D)) / (2 * a)
    print(f"The roots of the equation are {root1} and {root2}")
    
elif D == 0:
 	x = -b / (2*a)
 	print("The roots of the equation is ",x)

else :
	print(" No Root Found if D < 0 ")
	
'''	
	

import cmath

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

# Calculate the discriminant
D = (b**2 - 4*a*c)

# Find two solutions using the quadratic formula
if D > 0:
    root1 = (-b + cmath.sqrt(D)) / (2 * a)
    root2 = (-b - cmath.sqrt(D)) / (2 * a)
    print(f"The roots of the equation are {root1} and {root2}")

elif D == 0:
    x = -b / (2 * a)
    print("The root of the equation is", x)

else:
    print("No real roots found if D < 0")

	