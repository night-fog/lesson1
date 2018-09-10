numbers = list(range(2,7))
print(str(numbers))
numbers.append('слово_в_конец_словаря')
print(str(len(numbers)))

print(numbers[0])
print(numbers[-1])
print(numbers[1:4])
numbers.remove('слово_в_конец_словаря')
