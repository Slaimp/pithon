sequence = input("Введите строку с последовательностью чисел: ")

digit_count = {}

for char in sequence:
    if char.isdigit():
        digit = int(char)
        digit_count[digit] = digit_count.get(digit, 0) + 1

print(digit_count)
