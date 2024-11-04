def separate_words_by_length(text):
    words = text.split()
    even_words = [word for word in words if len(word) % 2 == 0]
    odd_words = [word for word in words if len(word) % 2 != 0]
    print("Слова парної довжини:")
    print('\n'.join(even_words))
    print("Слова непарної довжини:")
    print('\n'.join(odd_words))

text = input("Введіть рядок: ")
separate_words_by_length(text)
