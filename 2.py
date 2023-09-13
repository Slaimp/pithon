def count_letter_pairs_and_vowels(word):
    upper_lower_pairs = 0
    vowels_count = 0

    for i in range(1, len(word)):

        if word[i].islower() and word[i - 1].isupper():
            upper_lower_pairs += 1
        elif word[i].isupper() and word[i - 1].islower():
            upper_lower_pairs += 1

        if word[i].lower() in "aeiou":
            vowels_count += 1

    return upper_lower_pairs, vowels_count


word = input("Введите слово: ")

pairs, vowels = count_letter_pairs_and_vowels(word)

print(f"Количество пар рядом стоящих букв верхнего и нижнего регистров: {pairs}")
print(f"Количество гласных букв в слове: {vowels}")
