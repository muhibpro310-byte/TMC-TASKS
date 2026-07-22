name = "Ali"
print("Hello,", name)
quote = "He said, \"I want to eat an apple.\""
print(quote)
names = "Harry,Subham"
print("Slice (0:4):", names[0:4])
fruit = "Mango"
print("Length of Mango:", len(fruit))
myname = "Sikander Hayat"
print("Slice (3:7):", myname[3:7])
text = "harry"
print("Upper:", text.upper())
text2 = "THIS IS YOUR PEN"
print("Lower:", text2.lower())
text3 = "!!!!Hayat!!!!!!!!"
print("Remove ! from right:", text3.rstrip("!"))
sentence = "Python is fun to learn"
print("Split:", sentence.split())
heading = "introduction to python"
print("Capitalize:", heading.capitalize())
word = "Welcome"
print("Centered:", word.center(20))
print("Count of 'o':", word.count("o"))
message = "hayat with"
print("Ends with 'th':", message.endswith("th"))
print("Find 'with':", message.find("with"))
code = "Code2026"
print("Is Alphanumeric:", code.isalnum())
numbers = [1, 2, 3, 4, 5]
print("\nOriginal List:", numbers)
numbers.append(6)
print("After Append:", numbers)
numbers.insert(2, 100)
print("After Insert:", numbers)
copy_list = numbers.copy()
print("Copied List:", copy_list)
numbers.extend([7, 8, 9])
print("After Extend:", numbers)
numbers.sort()
print("Sorted:", numbers)
numbers.reverse()
print("Reversed:", numbers)
print("Index of 100:", numbers.index(100))
print("Count of 6:", numbers.count(6))
tup = (1, 2, 3, 5, 9, 1)
print("\nTuple:", tup)
fruits = ("Apple", "Banana", "Cherry")
print("Fruits:", fruits)
green, yellow, red = fruits
print("Green:", green)
print("Yellow:", yellow)
print("Red:", red)
def calculate_gmean(a, b):
    return (a * b) ** 0.5
print("\nGeometric Mean of 9 and 10:", calculate_gmean(9, 10))
person = ["Maria", 29, "Data Engineer", "Spain"]
name, age, role, country = person
print("\nName:", name)
print("Age:", age)
print("Role:", role)
print("Country:", country)
set_a = {1, 2, 3, 4, 5}
set_b = {5, 3, 6, 7, 8, 1}
print("\nSet A:", set_a)
print("Set B:", set_b)
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference (A-B):", set_a - set_b)
print("Symmetric Difference:", set_a ^ set_b)
print("\nProgram Completed Successfully!")
