def get_summ(one, two, delimiter='&'):
    two = str(two).upper()
    return str(one) + str(delimiter) + two


a = 'Learn'
b = 'python'
sum_string = get_summ(one=a, two=b, delimiter='!')
print(sum_string)


'''
    Измените функцию get_summ() чтобы результат выводился заглавными буквами использйте метод 'строка'.upper()
    Вызовите функцию, пердав в нее два аргумента "Learn" и "python"
    Сохраните результат вызова функции в переменную sum_string
    Выведите на экран значение переменной

'''