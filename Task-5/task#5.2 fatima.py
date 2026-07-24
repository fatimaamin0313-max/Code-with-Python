sentence = input("Enter sentence:")
length = len(sentence)

print(sentence.upper())
print(sentence.lower())
print(sentence.title())
print(sentence.capitalize())


print("Total Number of Characters:",len(sentence))
print("Total Number of Words:",len(sentence.split()))