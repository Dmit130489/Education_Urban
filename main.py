# Задаем исходный список
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

# Инициализируем переменную для индекса
index = 0

# Цикл while для перебора элементов списка
while index < len(my_list):
    # Проверяем, что элемент не отрицательный
    if my_list[index] >= 0:
        # Выводим положительный элемент
        print(my_list[index])
    else:
        # Прерываем цикл, если встретили отрицательное число
        break
    # Увеличиваем индекс на 1 для перехода к следующему элементу
    index += 1

# print(len(my_list))