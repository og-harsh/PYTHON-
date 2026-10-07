# ==========================================
# 1. BASIC if / else
# ==========================================
age = 18 

if age >= 18:
    # Notice the space before print!
    # It tells python this code belongs inside the 'if
    print("you are an adult. You can vote!")
else:
    print("you are a minor. You cannot vote yet.")
    
    
# ==========================================
# 2. if / elif / else (Multiple Conditions)
# ==========================================
traffic_light = "Yellow"

if traffic_light == "Red":
    print("stop! your vehicle.")

elif traffic_light == "Yellow":
    print("slow down and get ready to stop.")
    
elif traffic_light == "Green":
    print("you can go now.") 
    
else: 
    print("invalid color! traffic light might be brokken.")       

# ==========================================
# 3. NESTED CONDITIONS (Condition inside a condition)
# ==========================================
has_ticket = True
is_vip = False

if has_ticket:
    print("Welcome to the concert!")

    # Checking another condition inside the first one
    if is_vip:
        print("Please go to the VIP lounge.")
    else:
        print("Please go to the general seating area.")
else:
    print("sorry, you need a ticket to enter.")
    

