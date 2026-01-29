# ==============================
# CONDITIONAL STATEMENTS
# ==============================

age = 20

if age >= 18:
    print("You are eligible to vote")
elif age == 17:
    print("You will be eligible next year")
else:
    print("You are not eligible to vote")


# ==============================
# LOOPING STATEMENTS
# ==============================

# for loop
for i in range(1, 6):
    print("For loop iteration:", i)

# while loop
count = 1
while count <= 5:
    print("While loop iteration:", count)
    count += 1


# ==============================
# LOOP CONTROL STATEMENTS
# ==============================

for i in range(1, 6):
    if i == 3:
        continue   # skips current iteration
    if i == 5:
        break      # exits loop
    print("Control statement value:", i)


# ==============================
# FUNCTIONS
# ==============================

def greet(name):
    return f"Hello, {name}"

print(greet("Ayan"))


# ==============================
# INPUT AND OUTPUT
# ==============================

user_name = input("Enter your name: ")
print("Welcome", user_name)


# ==============================
# EXCEPTION HANDLING
# ==============================

try:
    num = int("10")
    # num = int("0")
    # num = int("abc")
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
finally:
    print("Execution completed")


# ==============================
# LIST COMPREHENSION
# ==============================

squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)


# ==============================
# DICTIONARY ITERATION
# ==============================

student = {
    "name": "Ayan",
    "age": 25,
    "course": "AI & ML"
}

for key, value in student.items():
    print(key, ":", value)


# ==============================
# FILE HANDLING (BASIC)
# ==============================

with open("sample.txt", "w") as file:
    file.write("Hello Python")

with open("sample.txt", "r") as file:
    print(file.read())
