# ============================================================
# 1. LAMBDA FUNCTIONS
# ============================================================
print("\n--- Lambda Functions ---")
# Add 10 to a number
add_ten = lambda number: number + 10
print("5 + 10 =", add_ten(5))
# Multiply two numbers
multiply = lambda first, second: first * second
print("5 × 6 =", multiply(5, 6))
# Add two numbers
add = lambda first, second: first + second
print("10 + 20 =", add(10, 20))
# Find the larger of two numbers
larger_number = lambda first, second: first if first > second else second
print("Larger number:", larger_number(10, 20))
# Find the largest of three numbers
largest_number = lambda first, second, third: (
    first
    if first >= second and first >= third
    else second
    if second >= third
    else third
)
print("Largest number:", largest_number(10, 25, 15))
# ============================================================
# 2. FILTER FUNCTION
# ============================================================
print("\n--- Filter Function ---")
numbers = [1, 2, 3, 4, 5]
even_numbers = list(
    filter(lambda number: number % 2 == 0, numbers)
)
print("Original numbers:", numbers)
print("Even numbers:", even_numbers)
# ============================================================
# 3. MAP FUNCTION
# ============================================================
print("\n--- Map Function ---")
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(
    map(lambda number: number**2, numbers)
)
print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
# Using map() with a normal function
def combine_words(first_word, second_word):
    """Combine two words with a space."""
    return first_word + " " + second_word
fruits_group_one = ("apple", "banana", "cherry")
fruits_group_two = ("orange", "lemon", "pineapple")
combined_fruits = list(
    map(combine_words, fruits_group_one, fruits_group_two)
)
print("Combined fruits:", combined_fruits)
# ============================================================
# 4. NORMAL FUNCTIONS
# ============================================================
print("\n--- Normal Functions ---")
def count_items(items):
    """Return the total number of items."""
    return len(items)
fruits = ("apple", "banana", "cherry")
total_fruits = count_items(fruits)
print("Fruits:", fruits)
print("Total fruits:", total_fruits)
# ============================================================
# 5. EXCEPTION HANDLING
# ============================================================
print("\n--- Exception Handling ---")
def divide_numbers(first_number, second_number):
    """Divide two numbers safely."""
    try:
        result = first_number / second_number
    except ZeroDivisionError:
        print("Error: A number cannot be divided by zero.")
        return None
    except TypeError:
        print("Error: Both values must be numbers.")
        return None
    else:
        print("Division successful.")
        return result
    finally:
        print("Division operation finished.")
division_result = divide_numbers(10, 2)
if division_result is not None:
    print("Result:", division_result)
# Handling an invalid list index
student_marks = [70, 85, 90, 75, 88]
try:
    print("Selected mark:", student_marks[31])
except IndexError:
    print("Error: The requested list index does not exist.")
# ============================================================
# 6. FILE HANDLING
# ============================================================
print("\n--- File Handling ---")
def write_file(file_name, content):
    """Write content to a file."""
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(content)
    except OSError as error:
        print("Unable to write the file:", error)
    else:
        print(f"Data successfully written to '{file_name}'.")
def append_file(file_name, content):
    """Append content to a file."""
    try:
        with open(file_name, "a", encoding="utf-8") as file:
            file.write(content)
    except OSError as error:
        print("Unable to append to the file:", error)
    else:
        print(f"Data successfully appended to '{file_name}'.")
def read_file(file_name):
    """Read and display the contents of a file."""
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: '{file_name}' was not found.")
    except OSError as error:
        print("Unable to read the file:", error)
    else:
        print("\nFile contents:")
        print(content)
file_name = "python_practice.txt"
write_file(
    file_name,
    "Hello\n"
    "Welcome to Python file handling.\n"
    "This file was created using Python.\n"
)
append_file(
    file_name,
    "This line was added using append mode.\n"
)
read_file(file_name)
# ============================================================
# 7. CLASSES AND OBJECTS
# ============================================================
print("\n--- Classes and Objects ---")
class Person:
    """Represent a person with personal information."""
    def __init__(self, name, age, city=None, country=None):
        self.name = name
        self.age = age
        self.city = city
        self.country = country
    def introduce(self):
        """Display an introduction message."""
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    def display_address(self):
        """Display the city and country if provided."""
        if self.city and self.country:
            print(f"I live in {self.city}, {self.country}.")
        else:
            print("Address information is not available.")
    def __str__(self):
        """Return a readable representation of the object."""
        return f"{self.name} ({self.age} years old)"
person_one = Person("Ali", 20)
print("Name:", person_one.name)
print("Age:", person_one.age)
person_one.introduce()
person_one.display_address()
person_two = Person(
    name="Alyan",
    age=20,
    city="Lahore",
    country="Pakistan",
)
person_two.introduce()
person_two.display_address()
print("Person object:", person_two)
# ============================================================
# 8. STUDENT CLASS
# ============================================================
print("\n--- Student Class ---")
class Student:
    """Represent a student."""
    def __init__(self, name, student_id, marks):
        self.name = name
        self.student_id = student_id
        self.marks = marks
    def greet(self):
        """Greet the student."""
        print(f"Hello, {self.name}!")
    def calculate_average(self):
        """Calculate and return the student's average marks."""
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)
    def display_information(self):
        """Display complete student information."""
        print(f"Student name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.calculate_average():.2f}")
    def __str__(self):
        """Return a readable representation of the student."""
        return f"{self.name} — ID: {self.student_id}"
student_one = Student(
    name="Ahmed",
    student_id="CS-101",
    marks=[78, 85, 90, 82],
)
student_one.greet()
student_one.display_information()
print("Student object:", student_one)
# ============================================================
# PROGRAM COMPLETED
# ============================================================
print("\n--- Program Completed Successfully ---")