#module
# import math
# import random

# #using the math module to calculate the square root of 25    
# square_root = math.sqrt(25)
# print(f"The square root of 25 is: {square_root}")

# # Using the random module to generate a random number
# lucky_number = random.randint(1, 100)
# print(f"Your lucky number is: {lucky_number}")

from colorama import Fore

# Changing text color using the external colorama module
print(Fore.RED + "This text is red!")
print(Fore.GREEN + "Now the text is green!")
print(Fore.RESET + "And back to normal default color.")