Colleges = [
    [101, "Punjab College", "Lahore", 5000],
    [102, "Superior College", "Islamabad", 3500],
    [103, "Govt College", "Karachi", 4200]
]

print("Complete List of Colleges:")
print(Colleges[0])
print(Colleges[1])
print(Colleges[2])

print("\nDetails of First College:")
print(Colleges[0])

print("\nName of Second College:")
print(Colleges[1][1])

print("\nCity of Third College:")
print(Colleges[2][2])

Colleges[1][3] = 4000
print("\nUpdated Student Count of Second College:")
print(Colleges[1])

New_College = [104, "City College", "Faisalabad", 2800]
Colleges.append(New_College)

print("\nAfter Adding New College:")
print(Colleges[0])
print(Colleges[1])
print(Colleges[2])
print(Colleges[3])

Colleges.pop(0)

print("\nAfter Removing First College:")
print(Colleges[0])
print(Colleges[1])
print(Colleges[2])

print("\nTotal Number of Colleges:")
print(len(Colleges))

print("\nFinal Updated List:")
print(Colleges[0])
print(Colleges[1])
print(Colleges[2])