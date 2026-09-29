# ==========================================
# 1. String to Integer / Float
# =====================================
user_age_text = "20"
user_weight_text = "65.5"

# Converting string to integer (int)
age_number = int(user_age_text)
print(age_number + 5)

# Converting string to float
weight_number = float(user_weight_text)
print(weight_number - 2.0)

# ==========================================
# 2. Integer/Float to String (str)
# ==========================================
# Rule: You cannot combine text and numbers directly like this:
# print("My score is " + 100) -> This will throw an ERROR!

score = 100

# We must convert the integer to a string first
score_text = str(score)
print("My score is " + score_text)

# ==========================================
# 3. Float to Integer (Losing the decimal)
# ==========================================
price = 99.99

# Converting float to int just chops off the decimal part (it does NOT round up)
rounded_price = int(price)
print(rounded_price)

# ==========================================
# 4. Converting to Boolean (bool)
# ==========================================
# In Python, 0 or empty text "" is considered False. 
# Any other number or text is considered True.

print(bool(1))
print(bool(0))
print(bool("Harsh"))
print(bool(""))
