"""guessing number"""

SECRET = 2
FOUND = False
for i in range(1, 11, 1):
    if i == SECRET:
        FOUND = True
## you don't want to have an else statement inside the for loop here
# because then it would hit the else condition for every
# loop and that will make the code inefficient

if not FOUND:
    print("not found")
else:
    print("found number")
