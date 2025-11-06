def char_count(s):
    """s is a string of lowercase chars
    return a tuple where the first element is the number of vowels
    in s and the second element is the number of consonants in s
    """
    vowels = "aeiou"
    nvow = 0
    ncons = 0
    for char in s:
        if char in vowels:
            nvow += 1
        else:
            ncons += 1

    return (nvow, ncons)


(num_vowels, num_consonants) = char_count("ekeopre")

print("num vowels", num_vowels)
print("num consonants", num_consonants)
