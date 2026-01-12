age = int(input("Enter age: "))
has_id = input("Do you have ID? (yes/no): ").lower()

if age >= 18 and has_id == "yes":
    print("Allowed")
elif age >= 18 or has_id == "yes":
    print("Partially allowed")
else:
    print("Not allowed")
