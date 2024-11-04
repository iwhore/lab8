def replace_last_letter(text):
    words = text.split()
    modified_words = [word[:-1] + '_' if len(word) > 1 else word for word in words]
    return ' '.join(modified_words)

text = input("Введіть рядок: ")
print(replace_last_letter(text))
