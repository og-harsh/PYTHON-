# ==========================================
# 1. ARITHMETIC OPERATORS (For Math)
# ==========================================
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x**y)
print(x // 2)

# ==========================================
# 2. COMPARISON OPERATORS (Returns True or False)
# ==========================================
player_score = 80
high_score = 100

print(player_score == 80)
print(player_score != 80)
print(player_score > 80)
print(player_score < 80)
print(player_score >= 80)
print(player_score <= 80)

# ==========================================
# 3. LOGICAL OPERATORS (Combining Conditions)
# ==========================================
is_adult = True
has_license = True

# 'and' returns True ONLY if BOTH are True
print(is_adult and has_license)

# 'or' returns True if AT LEAST ONE is True
print(is_adult or has_license)

# 'not' reverses the result
print(not is_adult)

# ==========================================
# 4. ASSIGNMENT OPERATORS (Updating Values)
# ==========================================
health = 100
health -= 20
print(health)

health += 50
print(health)

# ==========================================
# 5. MEMBERSHIP OPERATORS (Checking if something exists)
# ==========================================
allowed_users = ["Harsh", "John", "Alice"]
print("Harsh" in allowed_users)
print("Bob" in allowed_users)