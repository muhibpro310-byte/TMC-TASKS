# ==========================
# Matrix (Upper Triangle)
# ==========================
num = [[5, 10, 8],
       [7, 6, 3],
       [2, 1, 9]]
print("Upper Triangle of Matrix:")
rows = len(num)
cols = len(num[0])

for i in range(rows):
    for j in range(cols):
        if j >= i:
            print(num[i][j], end=" ")
    print()
    
print("\nSet Example:")
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
# ==========================
# List Methods
# ==========================
print("\nList Methods:")
l1 = [1, 2, 3, 4, 5]
print("Original List:", l1)
# Append
l1.append(7)
print("After append(7):", l1)
# Count
print("Count of 2:", l1.count(2))
# Index
print("Index of 3:", l1.index(3))
# Sort
l1.sort()
print("After sort():", l1)
# Sort in reverse order
l1.sort(reverse=True)
print("After sort(reverse=True):", l1)
# Reverse the current order
l1.reverse()
print("After reverse():", l1)