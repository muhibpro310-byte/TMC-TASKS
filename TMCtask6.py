# ==========================
# Python Practice Script
# ==========================    
# --------------------------
# 1. Even or Odd Number
# --------------------------
x = int(input("Enter a number: "))
if x % 2 == 0:
    print(f"{x} is an Even number.")
else:
    print(f"{x} is an Odd number.")
# --------------------------
# 2. Functions
# --------------------------
# Simple function
def my_fun():
    print("\nHello from a function!")
my_fun()
# Function with parameter
def greet(name):
    print("Hello,", name)
greet("Email")
# Fahrenheit to Celsius
def find_celsius():
    far = float(input("\nEnter temperature in Fahrenheit: "))
    celsius = (far - 32) * 5 / 9
    print(f"Temperature in Celsius = {celsius:.2f}")
find_celsius()
# Celsius to Fahrenheit
def find_fahrenheit():
    cel = float(input("\nEnter temperature in Celsius: "))
    far = (cel * 9 / 5) + 32
    print(f"Temperature in Fahrenheit = {far:.2f}")
find_fahrenheit()
# --------------------------
# 3. Nested Loop
# --------------------------
print("\nNested Loop Example")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
for i in list1:
    for j in list2:
        print(i, j)
# --------------------------
# 4. Square Star Pattern
# --------------------------
print("\nSquare Pattern")
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()
# --------------------------
# 5. Right Triangle Pattern
# --------------------------
print("\nRight Triangle")
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
# --------------------------
# 6. Reverse Triangle Pattern
# --------------------------
print("\nReverse Triangle")
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
# --------------------------
# 7. Number Pattern
# --------------------------
print("\nNumber Pattern")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
# --------------------------
# 8. Pyramid Pattern
# --------------------------
print("\nPyramid Pattern")
n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(2 * i + 1):
        print("*", end=" ")
    print()
# --------------------------
# 9. Matrix Printing
# --------------------------
print("\nMatrix")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in range(3):
    for j in range(3):
        print(matrix[i][j], end=" ")
    print()
# --------------------------
# 10. Matrix Traversal
# --------------------------
print("\nMatrix Traversal")
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()
# --------------------------
# 11. Linear Search
# --------------------------
print("\nLinear Search")
arr = [1, 4, 9, 3, 5, 2, 10, 11, 12]
target = int(input("Enter value to search: "))
found = False
for i in range(len(arr)):
    if arr[i] == target:
        print(f"{target} found at index {i}")
        found = True
        break
if not found:
    print(f"{target} not found in the list.")
print("\nProgram Finished Successfully!")