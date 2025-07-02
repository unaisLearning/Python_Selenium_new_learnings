# find the grade of the student

# logic buiding
# step 1 input and output
# input -> mark -> float
# output - > string

# Rough logic
# if mark between
# A = 90-100
# B = 80 - 89
# C = 70 - 79
# D = 60 - 69
# F = 0 - 59
# Write code
try:
    mark = float(input("Enter mark of the student :"))

    if mark >= 90 and mark <= 100:
        print("your grade is A")
    elif mark >= 80 and mark <= 89:
        print("Your grade is B")
    elif mark >= 70 and mark <= 79:
        print("Your grade is C")
    elif mark >= 60 and mark <= 69:
        print("Your grade is D")
    elif mark > 100 or mark <= -1:
        print("it's not possible, write a valid mark")
    else:
        print("your grade is F")
except ValueError:
    print("write a valid numerical value")

# Edge cases


# optimise code
