# ==========================================
# VARIABLES & BASIC DATA TYPES
# ==========================================

# 1. string (str) - used for text, wrapped in single or double quotes.
first_name = "Harsh"
greeting = 'Welcome to python practice'

# 2. Integer (int) - whole number without decimals.
total_projects = 5
temperature = -2

# 3. Float (float) - Numbers with decimals points.
latop_price = 999.99
pi_value = 3.14159

# 4. Boolean (bool) - Represents True or Fales Values.
is_learning_python = True
is_game_over = False

# ==========================================
# ADVANCED DATA TYPES (Collections)
# ==========================================

# 5. List (list) - An ordered collection of items that you CAN change later.
tech_stack = ["python", "javascript", "react", "nodejs"]
tech_stack.append("django") #adding an item to the list.

# 6. Tuple ( tuple) - An ordered collection of items that you CANNOT change (immutables).
screen_resolutions = (1920, 1080)

# 7. Dictionary (dict) - A collection of key- value pairs, where each key is unique.
user_profile = {
    "username" : "Harsh",
    "age" : 20,
    "has_premium_account" : True
}

# ==========================================
# HOW TO CHECK A DATA TYPE
# ==========================================
# You can use the built-in type() function to check what kind of data a variable holds.
print(type(first_name))  # <class 'str'>
print(type(total_projects))  # <class 'int'>
print(type(latop_price))  # <class 'float'>
print(type(is_learning_python))  # <class 'bool'>
print(type(tech_stack))  # <class 'list'>
print(type(screen_resolutions))  # <class 'tuple'>
print(type(user_profile))  # <class 'dict'>