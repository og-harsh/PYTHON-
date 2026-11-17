import logging

logging.basicConfig(
    filename="student.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

name = input("Enter student name: ")

logging.info("Student application started")

print("Welcome", name)

logging.info("Student logged in successfully")

marks = int(input("Enter marks: "))

if marks >= 40:
    print("Student passed")
    logging.info("Student passed")

else:
    print("Student failed")
    logging.warning("Student failed")