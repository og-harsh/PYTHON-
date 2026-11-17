# ==========================================
# Program 1: SyntaxError Example
# ==========================================
# initialize the amount variable
amount = 10000

# check that You are eligible to
# purchase Dsa Self Paced or not
if amount > 2999:
    print("You are eligible to purchase Dsa Self Paced")


# ==========================================
# Program 2: ZeroDivisionError Example
# ==========================================
# initialize the amount variable
marks = 10000

try:
    a = marks / 0
    print(a)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

print("Rest of the program executed")


# ==========================================
# Program 3: TypeError Example
# ==========================================
x = 5
y = "hello"
z = x + y  # Raises a TypeError: unsupported operand type(s) for +: 'int' and 'str'


# ==========================================
# Program 4: Exception Handling Using try...except
# ==========================================
try:
    numerator = 10
    denominator = 0

    result = numerator / denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")
# Output: Error: Denominator cannot be 0.


# ==========================================
# Program 5: Catching Specific Exceptions
# ==========================================
# Program to handle multiple errors with one except statement
def fun(a):
    if a < 4:
        # throws ZeroDivisionError for a = 3
        b = a / (a - 3)
    # throws NameError if a >= 4
    print("Value of b = ", b)

try:
    fun(3)
    fun(5)
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")


# ==========================================
# Program 6: Try with Else Clause
# ==========================================
# program to print the reciprocal of even numbers
try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1 / num
    print(reciprocal)


# ==========================================
# Program 7: Python try...finally
# ==========================================
# program to print the reciprocal of even numbers with finally
try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1 / num
    print(reciprocal)
    print("else block is executed")
finally:
    print("always printed")


# ==========================================
# Program 8: Assert Statement
# ==========================================
def odd_even(n):
    assert (n % 2 == 0), " pass even number"
    print("Even Number")

odd_even(6)


# ==========================================
# Program 9: Raise an Exception (Example 1)
# ==========================================
# Python program to raise an exception
try:
    age = int(input("enter your age"))
    if age < 0:
        raise ValueError
    print("your age is ", age)
except ValueError:
    print("Enter valid age")
print("rest of code")


# ==========================================
# Program 10: Raise an Exception (Example 2)
# ==========================================
# Python program to raise an exception
# check_age function checks the age
def check_age(age):
    if age < 18:
        raise Exception(" Age must be 18 or above. ")
    else:
        print(" Age is valid. ")

try:
    check_age(17)
except Exception as e:
    print(" An error occurred: ", e)