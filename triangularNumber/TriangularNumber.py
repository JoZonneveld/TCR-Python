class TriangularNumber:
    def __init__(self, number):
        self.number = number

    def __calculate(self):
        return int(0.5 * self.number * (self.number+1))

    def divisible_by(self):
        calculated_number = self.__calculate()
        result = []

        for i in range(1, calculated_number+1):
            if calculated_number % i == 0:
                result.append(i)

        return result, len(result)


def run():
    length = 0
    iteration = 1
    while length < 10:
        t = TriangularNumber(iteration)
        divisible_list, length = t.divisible_by()
        print('Iteration: ' + str(iteration))
        print('List: ' + str(divisible_list))
        print('Divisible by: ' + str(length) + ' numbers \n')
        iteration += 1
