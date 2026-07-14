# 1. Create a list containing at least 5 favorite fruits
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print("Original List:", fruits)

# 3. Display the first fruit and the last fruit
print("First Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])

# 4. Display the total number of fruits
print("Total Number of Fruits:", len(fruits))

# 5. Add a new fruit to the end of the list
fruits.append("Pineapple")
print("After Adding Pineapple:", fruits)

# 6. Insert a fruit at the second position
fruits.insert(1, "Strawberry")
print("After Inserting Strawberry at 2nd Position:", fruits)

# 7. Remove any fruit from the list
fruits.remove("Banana")
print("After Removing Banana:", fruits)

# 8. Sort the list alphabetically
fruits.sort()
print("After Sorting Alphabetically:", fruits)

# 9. Reverse the list order
fruits.reverse()
print("After Reversing the List:", fruits)

# 10. Display the final updated list after each operation
print("Final Updated List after each operation:", fruits)