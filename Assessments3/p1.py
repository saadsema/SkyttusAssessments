#Take a string input and print its length.
str1 = input("Enter String :")
print("Length of String is : ",len(str1))

#Convert a sentence to lowercase.
print("this is a lower String :",str1.lower())

#Replace spaces with underscores in a string.
print(str1.replace(" ","_"))

#Extract the first and last character of a string.
print("First Character of a String :",str1[0])
print("Last Character of a String :",str1[-1])

#Reverse a string using slicing.
print(str1[::-1])

#Count how many times a letter appears in a string.
print(str1.count("d"))

#Check if a word is present in a sentence.
word ="hello"
c=0
if word in str1:
    print("word is present in a sentence")
else:
    print("not present in a sentence")

#Take name & age and print using f-string formatting.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"My name is {name} and I am {age} years old.")

#Remove extra spaces from the start and end of a string.
print("Removed Extra Spaces from String :", str1.strip())

#Join a list of words into a single string with - between them
words = ["Join", "a", "list", "of", "words"]
result = "-".join(words)
print(result)
