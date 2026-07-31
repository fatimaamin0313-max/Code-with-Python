Student_Name = input("Enter Student_Name : " )
Registration_Number = input("Enter Registration_Number : ")
Physics_Marks = float(input("Enter Physics_Marks : "))
Chemistry_Marks = float(input("Enter Chemistry_Marks : "))
Mathematics_Marks = float(input("Enter Mathematics_Marks : "))

Subject_Marks = [Physics_Marks , Chemistry_Marks , Mathematics_Marks]

Total_Marks = sum(Subject_Marks)
Average_Marks = Total_Marks / len(Subject_Marks)
Percentage = (Total_Marks / Total_Marks) * 100

if Percentage >= 90:
	grade = "A+"
elif Percentage >= 80:
	grade = "A"
elif Percentage >= 70:
	grade = "B"
elif Percentage >= 60:
	grade = "C"
elif Percentage >= 50:
	grade = "D"
else:
	grade = "F"

Upper_Name = Student_Name.upper()
Lower_Name = Student_Name.lower()
Title_Name = Student_Name.title()
Name_Length = len(Student_Name)

Student_Record = {"Registration Number": Registration_Number,
    "Student Name": Student_Name,
    "Physics": Physics_Marks,
    "Chemistry": Chemistry_Marks,
    "Mathematics": Mathematics_Marks,
    "Total Marks": Total_Marks,
    "Average Marks": Average_Marks,
    "Percentage": Percentage,
    "grade": grade}

print("\n=====Student_Record======")
print("Student_Name:", Student_Name)
print("Registration_Number:", Registration_Number)
print("\nSubject_Marks")
print("Physics:", Physics_Marks)
print("Chemistry:", Chemistry_Marks)
print("Mathematics:", Mathematics_Marks)

print("\nTotal_Marks:", Total_Marks)
print("Average_Marks:", round(Average_Marks, 2))
print("Percentage:", round(Percentage, 2))
print("grade:", grade)
print("grade:", grade)

print("\n=======String Operation=======")
print("Uppercase_Name:", Upper_Name)
print("Lowercase_Name:", Lower_Name)
print("Titlecase_Name:", Title_Name)
print("Name_Length:", Name_Length)
