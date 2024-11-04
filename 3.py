def remove_next_occurrences(text):
    words = text.split()
    modified_words = []
    for word in words:
        first_letter = word[0]
        modified_word = first_letter + word[1:].replace(first_letter, '')
        modified_words.append(modified_word)
    return ' '.join(modified_words)

text = input("Введіть речення: ")
print(remove_next_occurrences(text))
