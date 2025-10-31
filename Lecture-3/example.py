# find 4!

# while
# 4x3x2x1

# Step 1: Ask the user to enter a number
num = int(input("Enter a number: "))

# Step 2: Initialize a variable to store the factorial result
factorial = 1

# Step 3: Check if the number is negative, zero, or positive
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    # Step 4: Use a loop to multiply numbers from 1 to num
    for i in range(1, num + 1):
        print("value of i:", i)
        factorial = factorial * i
    # Step 5: Display the result
    print(f"The factorial of {num} is {factorial}")
