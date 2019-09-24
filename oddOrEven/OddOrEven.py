def odd_or_even(number):
    if number % 2 == 0:
        print(number, 'even')
    else:
        print(number, 'odd')


def run():
    number_list = [1, 3, 5, 4, 6, 8, 2, 3]
    for number in number_list:
        odd_or_even(number)
