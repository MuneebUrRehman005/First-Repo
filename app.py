print("hello world")


def calculate_total(price, tax_rate=0.15):
    tax_amount = price * tax_rate
    return price + tax_amount

# Get input from user
raw_price = input("Enter item price: ")

try:
    # 1. Try to parse the text into a decimal number
    price = float(raw_price)
    
    # 2. If parsing worked, run your function
    total = calculate_total(price)
    print("Total price with tax:", total)

except:
    # 3. If parsing failed, show this friendly message
    print("Error: Please enter numbers only (e.g., 50 or 99.95).")

def fullname(firstName,secondName):
    fullNAme = firstName + secondName
    return fullNAme

enterFirstName = input("Enter your first name: ")
enterSecondName = input("Enter you second name: ")
fullFull = fullname(enterFirstName, enterSecondName)

print(fullFull)


fruits = ["apple", "banana", "orange"]

# Accessing items (0-indexed)
print(fruits[0])   # apple
print(fruits[-1])  # orange (negative index gets from the end!)

# Adding items
fruits.append("grape")          # adds to the end
fruits = fruits + ["kiwi"]      # concatenation

# Slicing [start:stop]
print(fruits[1:3]) # ['banana', 'orange'] (up to, but not including index 3)


student = {
    "name": "Muneeb",
    "course": "TM351",
    "grade": 95
}

# Accessing values by key
print(student["name"])    # Muneeb

# Adding or updating a key-value pair
student["grade"] = 98
student["passed"] = True

# Looping through a dictionary
for key in student:
    print(key, "=", student[key])