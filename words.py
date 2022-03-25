"""
Step Two: Starting On Your Own
"""

# - For a list of words, print out each word on a separate line, but in all uppercase.
def print_upper_words(words):
    for word in words:
        print(word.upper())

# - Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).
def print_upper_words_2(words):
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word)

# - Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.
def print_upper_words_3(words, must_start_with):
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word)


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])
print_upper_words_2(["hello", "hey", "goodbye", "yo", "yes"])
print_upper_words_3(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})