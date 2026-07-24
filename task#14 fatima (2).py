students = {
    "student1": {"Registration Number": "2025-PSY-001",
                 "Name": "Sana",
                 "Department": "Psychology",
                 "Semester": 2,
                 "CGPA": 3.45},
    "student2": {"Registration Number": "2025-PSY-002",
                 "Name": "Sara",
                 "Department": "Psychology",
                 "Semester": 2,
                 "CGPA": 3.70},
    "student3": {"Registration Number": "2025-PSY-003",
                 "Name": "Hina",
                 "Department": "Psychology",
                 "Semester": 2,
                 "CGPA": 3.20},
    "student4": {"Registration Number": "2025-PSY-004",
                 "Name": "Fatima",
                 "Department": "Psychology",
                 "Semester": 2,
                 "CGPA": 3.80},
    "student5": {"Registration Number": "2025-PSY-005",
                 "Name": "Hira",
                 "Department": "Psychology",
                 "Semester": 2,
                 "CGPA": 3.60}}
print("Complete Nested Dictionary:")
print(students)

print("\nFirst Student Information:")
print(students["student1"])

print("\nName of Second Student:")
print(students["student2"]["Name"])

print("\nDepartment of Third Student:")
print(students["student3"]["Department"])

print("\nSemester of Fourth Student:")
print(students["student4"]["Semester"])

print("\nCGPA of Fifth Student:")
print(students["student5"]["CGPA"])

students["student1"]["CGPA"] = 3.90

print("\nUpdated CGPA of Student1:")
print(students["student1"]["CGPA"])

students["student1"]["University"] = "NUP University"

print("\nAfter Adding University:")
print(students["student1"])

# 11. Remove University fiel
students["student1"]["University"]

print("\nAfter Removing University:")
print(students["student1"])

# 12. Display keys and values of first student's record
print("\nKeys of First Student:")
print(students["student1"].keys())

print("\nValues of First Student:")
print(students["student1"].values())

# 13. Display final updated nested dictionary
print("\nFinal Updated Nested Dictionary:")
print(students)