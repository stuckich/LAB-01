# Запрос общих данных о заказе
order_name = input("Введите название заказа (например, Сувенирная мастерская): ")
customer_name = input("Введите имя заказчика: ")

# Запрос данных для Первой позиции (Значки)
pos1_name = input("Введите название первой позиции (Значки): ")
pos1_quantity = int(input("Введите количество для первой позиции: "))
pos1_price = float(input("Введите цену за единицу первой позиции: "))

# Запрос данных для Второй позиции (Брелоки)
pos2_name = input("Введите название второй позиции (Брелоки): ")
pos2_quantity = int(input("Введите количество для второй позиции: "))
pos2_price = float(input("Введите цену за единицу второй позиции: "))

# Запрос данных о доставке и оплате
delivery_cost = float(input("Введите стоимость доставки: "))
amount_paid = float(input("Введите внесенную сумму: "))

# Расчеты
pos1_cost = pos1_quantity * pos1_price
pos2_cost = pos2_quantity * pos2_price

total_items_cost = pos1_cost + pos2_cost
total_order_cost = total_items_cost + delivery_cost
total_quantity = pos1_quantity + pos2_quantity
change = amount_paid - total_order_cost

# Вывод результатов
print("\n" + "=" * 40)
print(f"Заказ: {order_name}")
print(f"Заказчик: {customer_name}")
print("=" * 40)

# Вывод позиций
print(f"{pos1_name} | {pos1_quantity} | {pos1_price:.2f} | {pos1_cost:.2f}")
print(f"{pos2_name} | {pos2_quantity} | {pos2_price:.2f} | {pos2_cost:.2f}")
print("-" * 40)

# Вывод итогов
print(f"Общее количество единиц: {total_quantity}")
print(f"Стоимость товаров без доставки: {total_items_cost:.2f} руб.")
print(f"Стоимость доставки: {delivery_cost:.2f} руб.")
print(f"Общая сумма с доставкой: {total_order_cost:.2f} руб.")
print(f"Внесено: {amount_paid:.2f} руб.")
print(f"Сдача: {change:.2f} руб.")
print("=" * 40)

