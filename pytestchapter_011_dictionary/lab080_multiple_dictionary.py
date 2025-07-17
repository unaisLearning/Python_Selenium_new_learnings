"""
we can create a dictionary inside of another dictionary..
"""

student1 = {
    "name" : "sam",
    "class": "SSLC",
    "age" : 16,
    "activities" :{
        "sport": "racing",
        "Arts" : "song"
    }
}
student2 = {
    "name" : "alex",
    "class": "9th",
    "age" : 15,
    "activities" :{
        "sport": "football",
        "arts" : "elocation"
    }
}
student_list = [student1,student2]
print(student_list)
print(student_list[0])
print(student_list[1])
print(student_list[0]["name"])
print(student_list[0]["activities"])
print(student_list[0]["activities"]["sport"])

#alternate way direct access from student2

print(student2["activities"]["arts"])
