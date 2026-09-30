def multiplication_chain(num):
    count_multy = 0
    while num >= 10:                 # пока число не станет однозначным
        product = 1
        while num > 0:
            product *= num % 10      # перемножаем цифры
            num //= 10               # убираем последнюю цифру
        num = product                # результат становится новым числом
        count_multy += 1             # считаем итерацию
    return count_multy


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    39, 4, 25, 999, 5050, 222333444
]

test_data = [
    3, 0, 2, 4, 1, 4
]


for i, d in enumerate(data):
    assert multiplication_chain(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')