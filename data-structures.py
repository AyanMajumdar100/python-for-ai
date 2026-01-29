# ==============================
# PYTHON DATA STRUCTURES
# ==============================

# -------- LIST --------
numbers = [1, 2, 3, 4, 5]
# list → MUTABLE
numbers.append(6)          # modifying list
numbers[0] = 100

# -------- TUPLE --------
coordinates = (10, 20)
# tuple → IMMUTABLE
# coordinates[0] = 50  ❌ This would cause an error

# -------- SET --------
unique_numbers = {1, 2, 3, 4}
# set → MUTABLE
unique_numbers.add(5)
unique_numbers.remove(2)

# -------- DICTIONARY --------
student = {
    "name": "Ayan",
    "age": 25,
    "course": "AI & ML"
}
# dict → MUTABLE
student["age"] = 26
student["city"] = "Kolkata"

# -------- STRING --------
message = "Hello Python"
# string → IMMUTABLE
message = message + " World"   # creates a NEW string

# ==============================
# PRINTING RESULTS
# ==============================

print("List:", numbers, type(numbers))
print("Tuple:", coordinates, type(coordinates))
print("Set:", unique_numbers, type(unique_numbers))
print("Dictionary:", student, type(student))
print("String:", message, type(message))
