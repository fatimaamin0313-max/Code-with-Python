Students = ["Sana", "Saba", "Mariam", "Sara" , "Hina"]
print("Complete list:", Students )

print("Total Number of Students:", len(Students))

Students.append("Hira")
print("After Adding Hira:", Students)

Students.insert(0, "Amna")
print("After Inserting Amna at 1st Position:", Students)

Students.remove("Sana")
print("After Removing Sana:", Students)

Students[2] = "Sana"
print("After changing 3rd Student:", Students) 

Students.index("Hira") 
print("Position of Hira:", Students) 

Students.pop() 
print("After removing last:", Students)

print("Students:", len(Students))

print("Final Updated List :", Students)