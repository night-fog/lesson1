'''
Создайте функцию format_price которая принимает один аргумент price
Приведите price к целому числу (тип int)
Верните строку "Цена: ЧИСЛО руб."
Вызовите функцию, передав на вход 56.24 и положив результат в переменную display_price
Выведите display_price на экран
'''

def format_price(_jopa):
    print('Цена: {} руб.'.format(_jopa.round()))

display_price = input('введите число 56.24: ')
print(format_price(display_price))
