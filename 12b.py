def get_sum(num_one: int, num_two: int):
    try:
        return int(num_one) + int(num_two)
    except ValueError:
        return False

val1, val2 = input('Enter two numbers: ').split()
print(get_sum(val1, val2))
