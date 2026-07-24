Students = []
Number_Students = float(input("How many Student you want to enter?"))
count = 1

while count <= Number_Students:

    print("\nEnter Details of Student", count)

    Student_ID = input("Enter Student_ID: ")
    Student_Name = input("Enter Student_Name: ")
    Physics = float(input("Enter Physics Marks: "))
    Chemistry = float(input("Enter Chemistry Marks: "))
    Mathematics = float(input("Enter Mathematics Marks: "))

    count += 1

Total_Marks = Physics + Chemistry + Mathematics
Average = Total_Marks / 3
Percentage = (Total_Marks / 300) * 100

Student_record = { "Student ID": Student_ID,
        "Student Name": Student_Name,
        "Physics": Physics,
        "Chemistry": Chemistry,
        "Mathematics": Mathematics,
        "Total Marks": Total_Marks,
        "Average Marks": Average,
        "Percentage": Percentage}

Students.append(Student_record)        

count += 1
print("\n=======All Student Records======")
for Student in Students:
	print(Student)
print("\nTotal Number of Students Entered:", len(Students))	