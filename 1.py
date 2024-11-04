def count_first_letter_occurrences(text):
    first_letter = text[0].lower()
    count = text.lower().count(first_letter)
    return count

text = input("Введіть рядок: ")
print(f"Кількість входжень першої літери: {count_first_letter_occurrences(text)}")
