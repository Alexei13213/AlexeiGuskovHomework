# Принцип работы понятен.
# Другой метод нашел в интернете, изучил и сделал под себя.
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(str(num), 'FizzBuzz')
    elif num % 3 == 0:
        print(str(num), 'Fizz')
    elif num % 5 == 0:
        print(str(num), 'Buzz')
    else:
        print(num)

#
# print('\n'.join(str(num) + '-''FizzBuzz' if num % 3 == 0 and num % 5 == 0 else str(num) + '-' 'Fizz'
# if num % 3 == 0 else str(num) + '-' 'Buzz' if num % 5 == 0 else str(num) for num in range(1, 101)))




## Поставил числа 6 вместо 3, и 10 вместо 5.
# print('\n'.join(str(num) + '-''FizzBuzz' if num % 6 == 0 and num % 10 == 0 else str(num) + '-' 'Fizz'
# if num % 6 == 0 else str(num) + '-' 'Buzz' if num % 10 == 0 else str(num) for num in range(1, 101)))