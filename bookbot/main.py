def count_words(text):
    if len(text) == 0:
        return 0
    words = text.split()
    return len(words)


def count_letters(text):
    letters = text.lower()
    letter_count = {}
    for letter in letters:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    return letter_count


with open('books/frankenstein.txt') as f:
    book = f.read()
    print("--- Begin report of Frankenstein ---")
    print(count_words(book), "words found in the document")
    letter_count = count_letters(book)
    for v in letter_count:
        print(f"The '{v}' character appeared {letter_count[v]} times.")

        # print(f"The {i}: {v}")
