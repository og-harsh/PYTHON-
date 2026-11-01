#creating list
numbers = [10, 20, 30, 40, 50]
mixed = ["Harsh", 25, True, 3.14]

#indexing 
print(numbers[0])
print(numbers[-1])

#Slicing [start:stop:step]
print(numbers[1:4])  # Elements at index 1, 2, 3: [20, 30, 40]
print(numbers[:3])   # First three elements: [10, 20, 30]
print(numbers[::2])  # Every second element: [10, 30, 50]
print(numbers[::-1]) # Reversed list: [50, 40, 30, 20, 10]

#========================================
#Adding, Modifying, and Removing Elements
#========================================

fruits = ["apple", "banana", "cherry"]

# Modifying an element
fruits[1] = "blueberry"          # ['apple', 'blueberry', 'cherry']

# Adding elements
fruits.append("date")            # Adds to the end: ['apple', 'blueberry', 'cherry', 'date']
fruits.insert(1, "avocado")      # Inserts at index 1
fruits.extend(["fig", "grape"])  # Appends multiple items from another iterable

# Removing elements
fruits.remove("cherry")          # Removes first occurrence of value 'cherry'
popped_item = fruits.pop()       # Removes and returns last item ('grape')
first_item = fruits.pop(0)       # Removes and returns item at index 0 ('apple')
del fruits[0:2]                  # Deletes a slice of elements



