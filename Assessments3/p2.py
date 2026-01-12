# 1. Create a list of 5 favorite movies
movies = ["Inception", "Interstellar", "The Matrix", "The Dark Knight", "Parasite"]
print("Original movies list:", movies)

# 2. Add a new movie to the list
movies.append("Gladiator")
print("After adding a movie:", movies)

# 3. Remove the first movie from the list
movies.pop(0)
print("After removing the first movie:", movies)

# 4. Sort a list of numbers in ascending order
numbers = [45, 12, 89, 3, 22, 7]
numbers.sort()
print("Sorted numbers:", numbers)

# 5. Reverse a list
numbers.reverse()
print("Reversed numbers:", numbers)

# 6. Find the largest number in a list
largest_number = max(numbers)
print("Largest number:", largest_number)

# 7. Merge two lists into one
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print("Merged list:", merged_list)

# 8. Access the last element of a list without using index number
last_element = merged_list[-1]
print("Last element of merged list:", last_element)

# 9. Create a nested list and access a specific inner element
nested_list = [[10, 20], [30, 40], [50, 60]]
inner_element = nested_list[1][0]
print("Accessed inner element:", inner_element)

# 10. Count how many times an element appears in a list
count_list = [1, 2, 3, 2, 4, 2, 5]
count_of_two = count_list.count(2)
print("Number of times 2 appears:", count_of_two)

# 11. Create a tuple with 5 numbers
number_tuple = (5, 10, 15, 20, 25)
print("Tuple with 5 numbers:", number_tuple)
