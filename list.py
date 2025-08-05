# Step 1: Create an empty list
my_list = []
print("Created an empty list:", my_list)

# Step 2: Append elements 10, 20, 30, 40 in one line
my_list.extend([10, 20, 30, 40])
print(f"Appended 10, 20, 30, 40: {my_list}")

# Step 3: Insert 15 at the second position (index 1)
my_list.insert(1, 15)
print(f"Inserted 15 at index 1: {my_list}")

# Step 4: Extend the list with [50, 60, 70]
my_list.extend([50, 60, 70])
print(f"Extended list with [50, 60, 70]: {my_list}")

# Step 5: Remove the last element
removed_item = my_list.pop()
print(f"Removed the last element ({removed_item}): {my_list}")

# Step 6: Sort the list in ascending order
my_list.sort()
print(f"Sorted the list: {my_list}")

# Step 7: Find and print the index of value 30
index_of_30 = my_list.index(30)
print(f"Index of value 30: {index_of_30}")
