name = input("Enter Student Name: ")
length = len(name)

first_character = name[0]
last_character = name[length - 1]

middle_index = length // 2
middle_character = name[middle_index]

first_three_characters = name[0:3]


print("First character:", first_character)
print("Last character:", last_character)
print("Middle character:", middle_character)
print("First three characters:", first_three_characters)