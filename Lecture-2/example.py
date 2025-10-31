"""Guessing game"""

SECRET = 7
GUESS_LOWER_LIMIT = 1
GUESS_UPPER_LIMIT = 10
guess = int(
    input(f"Guess a number between {GUESS_LOWER_LIMIT} - {GUESS_UPPER_LIMIT}: ")
)
while guess != SECRET:
    if guess > SECRET:
        guess = int(input("too high try again"))
    elif guess > GUESS_UPPER_LIMIT or guess < GUESS_LOWER_LIMIT:
        guess = int(
            input(f"guess must be between {GUESS_LOWER_LIMIT}  - {GUESS_UPPER_LIMIT}: ")
        )
    elif guess < SECRET:
        guess = int(input("too low try again: "))

print("that's correct!")
