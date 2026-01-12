# Dictionary operations

# 1. Create a dictionary storing student names and marks
students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92
}
print("Initial dictionary:", students)

# 2. Add a new key-value pair to an existing dictionary
students["David"] = 88
print("\nAfter adding a new student:", students)

# 3. Delete a key-value pair from a dictionary
del students["Bob"]
print("After deleting a student:", students)

# 4. Merge two dictionaries into one
extra_students = {
    "Eve": 90,
    "Frank": 75
}
merged_dict = students | extra_students  
print("\nMerged dictionary:", merged_dict)

# 5. Check if a key exists in a dictionary
key_to_check = "Alice"
print(f"\nDoes '{key_to_check}' exist?", key_to_check in merged_dict)

# 6. Count word frequency in a given string using a dictionary
text = "apple banana apple orange banana apple"
words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("\nWord frequency:", word_count)

# 7. Find the key with the maximum value in a dictionary
max_key = max(merged_dict, key=merged_dict.get)
print("\nStudent with highest marks:", max_key, "-", merged_dict[max_key])

# 8. Reverse keys and values in a dictionary
reversed_dict = {value: key for key, value in merged_dict.items()}
print("\nReversed dictionary:", reversed_dict)

# 9. Update the value for a specific key
merged_dict["Alice"] = 95
print("\nAfter updating Alice's marks:", merged_dict)

# 10. Convert a list of tuples into a dictionary
tuple_list = [("Math", 90), ("Science", 85), ("English", 88)]
subject_marks = dict(tuple_list)
print("\nDictionary from list of tuples:", subject_marks)
