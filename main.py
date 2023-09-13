def is_decreasing_order(number):

    num_str = str(number)

    for i in range(len(num_str) - 1):
        if num_str[i] < num_str[i + 1]:
            return False

    return True

try:
    num = int(input("Введите натуральное число: "))

    if num > 0:
        if is_decreasing_order(num):
            print("Последовательность цифр упорядочена по убыванию.")
        else:
            print("Последовательность цифр не упорядочена по убыванию.")
    else:
        print("Введите натуральное число.")
except ValueError:
    print("Введите корректное натуральное число.")



