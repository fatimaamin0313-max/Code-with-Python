Subject_1 = input("Enter Subject_1: ")
Subject_2 = input("Enter Subject_2: ")
Subject_3 = input("Enter Subject_3: ")
Subject_4 = input("Enter Subject_4: ")
Subject_5 = input("Enter Subject_5: ")

Subjects = [Subject_1, Subject_2, Subject_3, Subject_4, Subject_5]

print("\nComplete Subject List:", Subjects)

print("\nFirst Subject :", Subjects[0])
print("Last Subject :", Subjects[-1])

New_Subject = input("\nEnter a new subject to add: ")
Subjects.append(New_Subject)
print("After Adding Subject:", Subjects)

Remove_Subject = input("\nEnter a subject to remove: ")
Subjects.remove(Remove_Subject)
print("After Removing Subject:", Subjects)

print("\nString Operations on First Subject:")
print("Uppercase:", Subjects[-2].upper())
print("Lowercase:", Subjects[-2].lower())
print("Title Case:", Subjects[-2].title())
print("Length:", len(Subjects[-2]))

print("\nFinal Updated Subject List:")
print(Subjects)