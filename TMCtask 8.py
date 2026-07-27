# Python Collections
# Dictionary
d = {"brand": "Ford", "Model": "Mustang", "Year": 2000}
print("Dictionary:", d)
# Dictionary using constructor
thisdict = dict(name="Ali", age=20, grade=10)
print("Constructor Dictionary:", thisdict)
# Access Dictionary Items
d2 = {"type": "Fruit", "Name": "Mango", "Price": 500}
print("Price:", d2["Price"])
print("Name:", d2.get("Name"))
print("Keys:", d2.keys())
# Add New Items
car = {"Type": "Car", "Name": "Grandy"}
car["color"] = "White"
car["year"] = 2020
print("Updated Car:", car)
print("Values:", car.values())
print("Items:", car.items())
# Check if Key Exists
if "Name" in car:
    print("Key 'Name' exists")
else:
    print("Key not found")
# Set
thisset = {"apple", "banana", "cherry", True, 1, 2}
print("Set:", thisset)
thisset2 = {"apple", "banana", "cherry", False, True, 0}
print("Set with False/0:", thisset2)
# List
l1 = ["cherry", "name", "Pakistan"]
l2 = ["Laptop", "Phone", "Mouse"]
print("List 1:", l1)
print("List 2:", l2)
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print("List with duplicates:", thislist)
# Enumerate
marks = [1, 2, 3, 4, 5, 6, 7]
print("\nEnumerate Example:")
for index, mark in enumerate(marks):
    print(index, mark)
    if index == 3:
        print("Ali Amazing")
# Zip
names = ["Ali", "Usman", "Ahmed"]
scores = [85, 92, 78]
result = list(zip(names, scores))
print("\nZip Result:", result)
# Lambda Functions
double = lambda x: x * 2
cube = lambda y: y ** 3
print("Double of 5:", double(5))
print("Cube of 3:", cube(3))
# Function as Argument
def apply(fx, value):
    return 6 + fx(value)
print("Apply Function:", apply(double, 5))
# Input Validation
while True:
    try:
        age = int(input("\nEnter your age: "))
        if age <= 0:
            print("Age must be greater than 0")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")
print("Your age is:", age)
# Map
numbers = [1, 2, 3, 5, 6]
new_list = list(map(cube, numbers))
print("Cube using map:", new_list)

# Try Except
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a number.")