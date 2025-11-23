# Ask the user for an expression (e.g. "2+2", "3.5*2", "2**3")
user_input = input("")

# -------------------------------
# CHECK IF THE OPERATOR IS "**"
# -------------------------------
# We check this first because "**" uses 2 characters
if "**" in user_input:
    index = user_input.index("**") # find the starting position of "**"
    num1_str = user_input[:index] # everything before the operator
    operator = "**"
    num2_str = user_input[index+2:] # skip 2 characters ("**") to get the second number

# ---------------------------------------
# OTHERWISE, CHECK FOR NORMAL OPERATORS
# +, -, *, /
# ---------------------------------------
else:
    for i, ch in enumerate(user_input):
        # If this character is any of the single-character operators
        if ch in ["+", "-", "*", "/"]:
            if ch == "-" and (i == 0 or user_input[i-1] in ["+", "-", "*", "/"]):
                continue
            operator = ch # store the operator
            index = i # store its position
            break

    # Split the input into the two numbers based on operator index
    num1_str = user_input[:index]
    num2_str = user_input[index+1:]

# -------------------------------
# CONVERT NUMBERS TO INT OR FLOAT
# -------------------------------
num1 = float(num1_str) if "." in num1_str else int(num1_str)
num2 = float(num2_str) if "." in num2_str else int(num2_str)

# -------------------------------
# CALCULATOR FUNCTION
# -------------------------------
def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0: # prevent division by zero
            return "Error: Division by zero"
        return num1 / num2
    elif operator == "**":
        return pow(num1, num2) # exponent operator

# Calculate the result
result = calculator(num1, num2, operator)

# -------------------------------
# CLEAN OUTPUT
# If result is a float like 4.0, convert to int (4)
# -------------------------------
if isinstance(result, float) and result.is_integer():
    result = int(result)

# Print final result
print(result)