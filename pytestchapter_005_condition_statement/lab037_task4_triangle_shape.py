"""
Task 14th Nov 2024 | If-elif Else
Triangle Classifier:
Write a program that classifies a triangle based on its side lengths.
 Given three input values representing the lengths of the sides,
  determine if the triangle is equilateral (all sides are equal)
  , isosceles (exactly two sides are equal, or scalene (no sides are equal).
Use an if-else statement to classify the triangle.
"""
#Logic setting formula
#step 1 - i/p and o/p

#input -> 3 number ->float
#output -> Text -> string

#step 2 Rough logic
"""
if a == b and a== c and b== c -> equilateral
else if a!==b and a==c  and c!==b -> isosceles
else if a!==b and a!==c and c!==b -> scalene
else 


"""
#Step 3 - code
side1 = float(input("Enter the length of the side 1 in cm : "))
side2 = float(input("Enter the length of the side 2 in cm : "))
side3 = float(input("Enter the length of the side 3 in cm : "))

if side1 == side2 and side1== side3 and side2== side3:
    print("your triangle is Equilateral")
elif side1 != side2 and side1 != side3 and side2 == side3:
    print("your triangle is isosceles")
elif side1 != side2 and side1 == side3 and side2 != side3:
    print("your triangle is isosceles")
elif side1 == side2 and side1 != side3 and side2 != side3:
    print("your triangle is isosceles")
elif side1 != side2 and side1 != side3 and side2 != side3:
    print("your triangle is scalene")
else:
    print("hmm..")
