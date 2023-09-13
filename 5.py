menu = {
    "торт": ["вкусный торт", 200, 100],
    "пирожное": ["нежное пирожное", 50, 300],
    "маффин": ["ароматный маффин", 75, 200],
    "пончик": ["сдобный пончик", 100, 150],
    "печенье": ["хрустящее печенье", 30, 500],
    "эклер": ["изысканный эклер", 80, 250]
}


def print_description():
    print("Описание продукции:")
    for product, description in menu.items():
        print(f"{product} - {description[0]}")


def print_prices():
    print("Цены на продукцию:")
    for product, data in menu.items():
        print(f"{product} - {data[1]} рублей за 100гр")


def print_quantities():
    print("Количество продукции:")
    for product, data in menu.items():
        print(f"{product} - {data[2]} грамм")


def print_all_info():
    print("Вся информация о продукции:")
    for product, data in menu.items():
        print(f"{product} - {data[0]}, Цена: {data[1]} рублей за 100гр, Количество: {data[2]} грамм")


def purchase():
    total_cost = 0
    while True:
        print("Для завершения покупки введите '0'")
        product = input("Введите название продукции: ")
        if product == '0':
            break
        if product in menu:
            try:
                quantity = int(input("Введите количество в граммах: "))
                if quantity <= menu[product][2] and quantity > 0:
                    cost = (quantity / 100) * menu[product][1]
                    total_cost += cost
                    menu[product][2] -= quantity
                    print(f"Вы добавили {quantity} грамм {product} в корзину за {cost} рублей.")
                else:
                    print("Извините, товара в таком количестве нет на складе.")
            except ValueError:
                print("Пожалуйста, введите корректное количество.")
        else:
            print("Извините, продукция с таким названием не найдена в меню.")

    print(f"Сумма вашей покупки составляет: {total_cost} рублей")


while True:
    print("\nМеню Кондитерской:")
    print("1. Просмотр описания")
    print("2. Просмотр цен")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. До свидания")

    choice = input("Выберите пункт меню: ")

    if choice == '1':
        print_description()
    elif choice == '2':
        print_prices()
    elif choice == '3':
        print_quantities()
    elif choice == '4':
        print_all_info()
    elif choice == '5':
        purchase()
    elif choice == '6':
        print("До свидания!")
        break
    else:
        print("Пожалуйста, выберите корректный пункт меню.")
