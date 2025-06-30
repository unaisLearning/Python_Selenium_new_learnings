#Find the area of the circle

#Logic Building

#step 1 - i/o
# input -> r , datatype -> float
# pi -> 3.14 , power = pow or **
# output -> area, datatype -> float

#Step 2 - Rough logic
# Area of circle = 3.14 * pow(r,2)

#step 3 - Code

radius = float(input("enter the radius of the circle :"))

area = 3.14159 * radius**2
print("Area of the circle is = ", area , "cm²")
#formated
print(f"Area of the circle {area :.2f} cm²")

#inbuild python function
import math
pi = math.pi
area2 = (pi * pow(radius, 2))
print(area2)

#oneline - NOT RECOMMENDED

print(3.14 * (float(input("enter the radius of the circle :")))**2)