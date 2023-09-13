input_str = input("Введите числа, разделенные пробелом: ")

input_list = input_str.split()

numbers = []

for item in input_list:
    try:
        number = int(item)
        numbers.append(number)
    except ValueError:
        print(f"Введенное значение '{item}' не является числом и будет проигнорировано.")

if numbers:
    positive_sum = sum(x for x in numbers if x > 0)

    first_zero_index = None
    for i, x in enumerate(numbers):
        if x == 0:
            first_zero_index = i
            break

    if first_zero_index is not None:
        sum_after_zero = sum(numbers[first_zero_index + 1:])
    else:
        sum_after_zero = "Сумму посчитать нельзя"

    numbers = [x for x in numbers if x >= 0]

    print("Сумма положительных элементов:", positive_sum)
    print("Сумма элементов после первого нуля:", sum_after_zero)
    print("Список после удаления отрицательных элементов:", numbers)
else:
    print("Список чисел пуст. Вы не ввели корректных чисел.")
