#Merge 2 dictionaries
dic1 = {"name" : "alex",
          "place" : "newyork",
          "age" : 4
        }
dic2 = {"class" : "UKG",
          "school" : "majmau",
          "busno" : 2}

stud = dic1 | dic2
print(stud)