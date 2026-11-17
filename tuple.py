#creating tuples
coords = (10, 20, 30, 40, 50)
packed = "Harsh", 25, True  # Tuple packing (parentheses are optional)

#The single - element tuple rule
not_a_tuple = (42)        # Type is int
single_tuple = (42,)       # Type is tuple (note the trailing comma)

#indexing and slincing (works just like lists)
print(coords[0])                    # First element: 10
print(coords[-1])                   # Last element: 50
print(coords[1:4])                  # Slice returns a new tuple: (20, 30, 40)
print(coords[::-1])                 # Reversed tuple: (50, 40, 30, 20, 10)-1])

#=========================
#Unpacking and Extended Unpacking
#=========================
user = ("Harsh", 42, "developer")
name, age, role = user
print(f"name='{name}', age={age}, role='{role}'")

#swapping vaariables without a temporary variable 
a, b = 5, 10 
a, b = b, a 
print(a)

#extnded unpacking with *
scores = (50, 60, 68, 92, 99)
lowest, *middle, highest = scores
print(lowest)
print(middle)
print(highest )






