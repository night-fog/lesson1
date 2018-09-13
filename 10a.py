import random


def is_int(value):
    try:
        if int(value):
            return True
    except ValueError:
        return False

def oracul(age: int):
    alternative_way = ['не проспи школу', 'пора в ПТУ']
    alternative_way2 = ['пора в универ', 'на работу пора']
    if age < 7:
        return 'пора в сад'
    elif age <= 15:
        return alternative_way[0]
    elif age <= 17:
        return random.SystemRandom().choice(alternative_way)
    elif age <= 22:
        return random.SystemRandom().choice(alternative_way2)
    elif age < 65:
        return alternative_way2[1]
    elif age >= 65:
        return 'в Вальгалу пора'

age = input('Enter your age: ')

age = int(age)
lifestyle = oracul(age)
print(lifestyle)
