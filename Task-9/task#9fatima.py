student_name = input("Enter Student Name: ")

m1 = float(input("Enter Subject 1 Marks: "))
m2 = float(input("Enter Subject 2 Marks: "))
m3 = float(input("Enter Subject 3 Marks: "))
m4 = float(input("Enter Subject 4 Marks: "))
m5 = float(input("Enter Subject 5 Marks: "))

marks_list = [m1, m2, m3, m4, m5]

print("\nFirst Subject Marks:", marks_list[0])
print("Last Subject Marks:", marks_list[4])

marks_list.append(100)
print("\nAfter Appending 100:", marks_list)

marks_list.remove(100)
print("After Removing 100:", marks_list)

total = sum(marks_list)
average = total / len(marks_list)
percentage = (total / 500) * 100
highest = max(marks_list)
lowest = min(marks_list)

upper_name = student_name.upper()
lower_name = student_name.lower()
name_length = len(student_name)

marks_set = set(marks_list)
print("\nOriginal Set:", marks_set)

extra_marks = {90, 95, 100}

print("Union:", marks_set.union(extra_marks))
print("Intersection:", marks_set.intersection(extra_marks))
print("Difference:", marks_set.difference(extra_marks))

print("\n" + "=" * 40)
print("      STUDENT RESULT REPORT")
print("=" * 40)

print("Student Name :", student_name)
print("Marks List   :", marks_list)
print("Total Marks  :", total)
print("Average      :", average)
print("Percentage   :", percentage, "%")
print("Highest Marks:", highest)
print("Lowest Marks :", lowest)

print("\nName Operations")
print("Uppercase :", upper_name)
print("Lowercase :", lower_name)
print("Length    :", name_length)

print("=" * 40)