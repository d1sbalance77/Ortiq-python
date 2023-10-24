while True:

    order_sum = float(input("Введите сумму заказа: $"))

    tax = order_sum * 0.2
    tip = (order_sum - tax) * 0.18

    total_number = order_sum + tax + tip

    print(f'Налог: ${tax}')
    print(f'Чаевые: ${tip}')
    print(f'Итоговая сумма: ${total_number}')
