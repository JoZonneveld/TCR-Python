from fibonacci.Fibonacci import fibonacci


def odd_or_even(number):
    if number % 2 == 0:
        print(number, 'even')
    else:
        print(number, 'odd')


def run():
    number_list = fibonacci(1, 20)
    for number in number_list:
        odd_or_even(number)
