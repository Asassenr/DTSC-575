import sys

def counter():
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = sys.argv[1]
    word = word.lower()
    word = word.strip()
    listed_word = list(word)
    found_vowels = []
    num_vals = 0

    for i in listed_word:
        if i in found_vowels:
            pass
        elif i in vowels:
            num_vals += 1
            found_vowels.append(i)
    print(num_vals)    

counter()