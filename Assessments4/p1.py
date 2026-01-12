# Tuple operations

# 1. Create a tuple with 5 numbers
numbers = (10, 20, 30, 40, 50)
print("Tuple:", numbers)

# 2. Access the third element in a tuple
print("Third element:", numbers[2])

# 3. Unpack a tuple into separate variables
a, b, c, d, e = numbers
print("Unpacked values:", a, b, c, d, e)


# Set operations

# 4. Create a set of 5 fruits
fruits = {"apple", "banana", "orange", "mango", "grape"}
print("\nInitial fruit set:", fruits)

# 5. Add a new fruit to the set
fruits.add("pineapple")
print("After adding a fruit:", fruits)

# 6. Remove an element from a set
fruits.remove("banana")
print("After removing a fruit:", fruits)

# 7. Find union of two sets
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "kiwi", "orange"}
union_set = set1.union(set2)
print("\nUnion of sets:", union_set)

# 8. Find intersection of two sets
intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)

# 9. Check if one set is a subset of another
subset_result = {"apple", "banana"}.issubset(set1)
print("Is subset:", subset_result)

# 10. Convert a list with duplicate values into a set to remove duplicates
duplicate_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(duplicate_list)
print("\nOriginal list:", duplicate_list)
print("Set after removing duplicates:", unique_set)
