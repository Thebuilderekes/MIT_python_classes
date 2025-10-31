word = input("enter a word: ")

enthusiasm_level = input("eneter an enthusiasm level pf 1-8: ")

for char in word:
    print(f"can i get a {char} : {char}")

print("what does it spell?")

for i in range(int(enthusiasm_level)):
    print(word + "!!!!")
