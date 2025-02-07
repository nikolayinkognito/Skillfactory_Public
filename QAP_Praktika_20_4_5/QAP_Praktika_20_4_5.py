import json
with open("orders_july_2023.json", "r", encoding="utf-8") as my_file:
    # считываем информацию из файла и преобразовываем строку json в словарь
    orders_july_2023 = json.load(my_file)
#print(orders_july_2023)

            # 1. Какой номер самого дорого заказа за июль?

max_price = 0
max_order = ''
# Проходим по всем заказам за июль
for order_num, orders_data in orders_july_2023.items():
    # получаем стоимость заказа
    price = orders_data['price']
    # если стоимость больше максимальной - запоминаем номер и стоимость заказа
    if price > max_price:
        max_order = order_num
        max_price = price
print('1. Какой номер самого дорого заказа за июль?')
print(f'Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}')

            # 2. Какой номер заказа с самым большим количеством товаров?

max_quantity = 0
max_order = []  # Теперь это будет список, чтобы хранить все заказы с максимальным количеством

# Проходим по всем заказам за июль
for order_num, orders_data in orders_july_2023.items():
    # Получаем количество товаров
    quantity = orders_data['quantity']

    # Если количество больше максимального - запоминаем номер и количество товара
    if quantity > max_quantity:
        max_quantity = quantity
        max_order = [order_num]  # Запоминаем только что найденный максимальный заказ
    elif quantity == max_quantity:
        # Добавляем номер заказа в список, если количество равно максимальному
        max_order.append(order_num)

# Создаем список с информацией о заказах с максимальным количеством товаров
orders_list = []
print('2. Какой номер заказа с самым большим количеством товаров?')
for order_num in max_order:
    orders_list.append(
        f'Номер заказа с самым большим количеством товара: {order_num} '
        f'количество товара: {orders_july_2023[order_num]['quantity']}'
    )

# Выводим список
print('\n'.join(orders_list))

            # 3. В какой день в июле было сделано больше всего заказов?

# Инициализируем словарь для хранения количества заказов по дням
summ_date = {}

# Проходим по всем заказам за июль
for order_num, orders_data in orders_july_2023.items():
    # Получаем дату заказа
    order_date = orders_data.get('date', None)

     # Увеличиваем счетчик для данной даты, если она уже есть в словаре
    summ_date[order_date] = summ_date.get(order_date, 0) + 1

# Находим максимальное количество заказов
max_count = max(summ_date.values())

# Выводим даты с максимальным количеством заказов
max_date_list = [date for date, count in summ_date.items() if count == max_count]
print('3. В какой день в июле было сделано больше всего заказов?')
for date in max_date_list:
    print(f"Больше всего заказов было сделано: {date}: Количество заказов: {summ_date[date]} ")

            # 4. Какой пользователь сделал самое большое количество заказов за июль?

# Инициализируем словарь для хранения количества заказов по дням
summ_user_id = {}

# Проходим по всем заказам за июль
for order_num, orders_data in orders_july_2023.items():
    # Получаем список пользователей
    order_user_id = orders_data.get('user_id', None)

     # Увеличиваем счетчик для пользователя, если он уже есть в словаре
    summ_user_id[order_user_id] = summ_user_id.get(order_user_id, 0) + 1

# Находим максимальное количество заказов
max_count = max(summ_user_id.values())

# Выводим пользователей с максимальным количеством заказов
max_user_id_list = [user_id for user_id, count in summ_user_id.items() if count == max_count]
print('4. Какой пользователь сделал самое большое количество заказов за июль?')
for user_id in max_user_id_list:
    print(f"Больше всего заказов было сделано: {user_id}: Количество заказов: {summ_user_id[user_id]} ")

            # 5. У какого пользователя самая большая суммарная стоимость заказов за июль?

# Инициализируем словарь для хранения количества заказов по дням
summ_user_id = {}

# Проходим по всем заказам за июль
for order_num, orders_data in orders_july_2023.items():
    # Получаем идентификатор пользователя и стоимость заказа
    user_id = orders_data.get('user_id', None)
    order_price = orders_data.get('price', 0)

    # Увеличиваем стоимость для пользователя, если он уже есть в словаре
    summ_user_id[user_id] = summ_user_id.get(user_id, 0) + order_price

# Находим максимальное количество заказов
max_total_cost = max(summ_user_id.values())
max_user_id_list = [user_id for user_id, cost in summ_user_id.items() if cost == max_total_cost]
print('5. У какого пользователя самая большая суммарная стоимость заказов за июль?')
# Выводим пользователя с максимальной суммарной стоимостью заказов
for user_id in max_user_id_list:
    print(f"Большая суммарная стоимость заказов у пользователя: {user_id}: "
          f"общая стоимость: {summ_user_id[user_id]} ")

            # 6. Какая средняя стоимость заказа была в июле?

total_orders_value = 0 # сумма всех заказов
order_count = 0 # счётчик заказов
# Проходим по всем заказам за июль
for order_num, orders_data in orders_july_2023.items():
    # Получаем идентификатор пользователя и стоимость заказа
    order_price = orders_data.get('price', 0)

    # Суммируем общую стоимость всех заказов
    total_orders_value += order_price
    # Увеличиваем счетчик заказов
    order_count += 1

# Вычисляем среднюю стоимость заказа
average_order_price = total_orders_value / order_count
print('6. Какая средняя стоимость заказа была в июле?')
print("Средняя стоимость заказа в июле:", average_order_price)

            # 7. Какая средняя стоимость товаров в июле?

# Инициализируем переменные для суммы всех заказов и количества заказов
total_items_value = 0
item_quantity = 0

# Проходим по всем заказам за июль
for order_num, orders_data in orders_july_2023.items():
    # Получаем идентификатор пользователя, стоимость заказа и количество товаров
    user_id = orders_data.get('user_id', None)
    order_price = orders_data.get('price', 0)
    quantity = orders_data.get('quantity', 0)

    # Увеличиваем общую стоимость всех товаров
    total_items_value += order_price * quantity

    # Увеличиваем счетчик товаров
    item_quantity += quantity

# Вычисляем среднюю стоимость товаров в июле
average_order_price = total_orders_value / item_quantity
print('7. Какая средняя стоимость товаров в июле?')
print("Средняя стоимость товаров в июле:", average_order_price)