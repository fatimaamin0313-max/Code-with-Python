Student_Name = input("Enter Student Name: ")
Physics_Marks = float(input("Enter Physics Marks: "))
Chemistry_Marks = float(input("Enter Chemistry Marks: "))
Mathematics_Marks = float(input("Enter Mathematics Marks: "))

Student_data = {
    "Name": Student_Name,
    "Physics": Physics_Marks,
    "Chemistry": Chemistry_Marks,
    "Mathematics": Mathematics_Marks}

print("\n--- Complete Dictionary ---")
print(Student_data)
print("\nStudent Name:", Student_data["Name"])
print("Physics Marks:", Student_data["Physics"])
print("Chemistry Marks:", Student_data["Chemistry"])
print("Mathematics Marks:", Student_data["Mathematics"])


total_marks = (
    Student_data["Physics"]
    + Student_data["Chemistry"]
    + Student_data["Mathematics"]
)

average_marks = total_marks / 3
percentage = (total_marks / 300) * 100

print("\n--- Result ---")
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Percentage:", percentage, "%")


New_Physics_Marks = float(input("\nEnter Updated Physics Marks: "))
Student_data["Physics"] = New_Physics_Marks
Student_data["Grade"] = "A"
print("\nDictionary After Adding Grade:")
print(Student_data)

Student_data.pop("Grade")
print("\nDictionary Keys:")
print(Student_data.keys())

print("\nDictionary Values:")
print(Student_data.values())

print("\n--- Final Updated Dictionary ---")
print(Student_data)
print("\n--- Final Updated Dictionary ---")
print(Student_data)

