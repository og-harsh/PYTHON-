# ==========================================
# 1. CREATING STRINGS
# ==========================================
# 1. CREATING STRINGS
# ==========================================
# You can use single quotes or double quotes (both work the exact same way)
first_name = 'Harsh'
last_name = 'Khuttan'

# for multi-line text ( lika a paragaph), use triple quotes (''' or """)
bio = """I am a web developer.
I know HTML, CSS, JavaScript and now I am learning PYthon.
I love designing and creating paintings in my free time."""

# ==========================================
# 2. F-STRINGS (String Formatting) - VERY IMPORTANT
# ==========================================
# Placing an 'f' before the quotes allows you to inject variables directly inside {}
# (We used this in your Calculator code!)
age = 20 
greeting = f"Hello, my name is {first_name} and I aam {age} years old."
print(greeting)

# ==========================================
# 3. STRING METHODS (Built-in functions for text)
# ==========================================
message = "python is AWESOME!"

# len() - counts the total number of characters (including spaces)
print(len(message))

#upper() - makes everthing CAPITAL
print(message.upper())

#lower() - makes everything lowercase
print(message.lower())

#strip() - removes extra spaces from the start and end 
print(message.strip())

#.replace() - changes a sprcific word
print(message.replace("AWESOME", "EASY"))

# ==========================================
# 4. STRING INDEXING & SLICING (Extracting parts of text)
# ==========================================
# In Python, counting always starts from 0, not 1.

word = "DEVELOPER"

print(word[0])  # D
print(word[1])  # E
print(word[2])  # V
print(word[3])  # E
print(word[4])  # L
print(word[5])  # O
print(word[6])  # P
print(word[7])  # E
print(word[8])  # R

# Slicing - Extracting a portion of the string
print(word[0:5])  # DEVEL
print(word[3:8])  # ELOPE
print(word[:5])   # DEVEL
print(word[3:8])  # ELOPE
print(word[3:])   # ELOPER
