#Eligibility to check go to Goa

#Logic building Formula

#step 1 - i/p and o/p
#input datatype - int
#output -> string

#step 2 - Rough Logic (brute force (what first come to your mind))
# age < 18 -> not allowed in club
# age > 18 -> allowed in club

#step 3 - write the code
try:
    age = int(input("Enter your age :"))

    if age < 0 or age > 130:
        print("invalid input")
    elif age < 18:
        print("you are not eligible to club")
    else:
        print("you are eligible for club")
except ValueError:
    print("Enter only numeric value")
#Step 4 - Check for the edge cases
#character entry - ABC
#Negative number entry
#above 130 age entry


#step 5 - Optimise the code
#handle all the edges
#already did