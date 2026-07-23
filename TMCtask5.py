import random
while True:
    x = input("Enter your value (q to exit): ")
    if x == 'q':
        print("Program exited.")
        break
    else:
        print("You entered:", x)
while True:
    print("Run infinite:")
    break
x = random.randint(1, 10)
print("Random number 1-10:", x)
y = random.randint(20, 30)
print("Random number 20-30:", y)
z = random.randrange(2, 12)
print("Random range 2-11:", z)
my_num = [7, 14, 21, 42, 99]
chosen_number = random.choice(my_num)
print("Chosen number:", chosen_number)
x = random.randrange(2, 15)
print("Random number 2-14:", x)
arr = [1, 4, 9, 3, 5, 2, 10, 11, 12]
target = int(input("Enter your value = "))
for i in range(len(arr)):
    if arr[i] == target:
        print(f"Your target {target} is present at index {i}")
        break
else:
    print(f"{target} target is not found.")