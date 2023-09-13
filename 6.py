import random

a = [random.randint(-10, 10) for i in range(10)]
b = tuple(a)
print(b)
i = 0

for number in b:
    if number > 0:
        i += 1

print(f"Количество положительных элементов в списке: {i}")
