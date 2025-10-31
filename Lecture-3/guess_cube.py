"""find cube root"""

num = int(input("enter a number: "))
FOUND = False
CUBE_ROOT = 0
for i in range(1, 10):
    if i**3 == num:
        print(f"{i}")
        FOUND = True
        CUBE_ROOT = i
        print(f"the cube root of {num} is {i}")
        break
    # We break because we dont what it checking all the numbers 
    #in the range, just up until it finds what it is looking for

if num < 0:
    print("your number does not have a cube root")
elif num == 0:
    print(f"the cube root of {num} is 0")
elif not FOUND:
    print("cannot find cube root")
