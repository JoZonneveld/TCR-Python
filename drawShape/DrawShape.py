class DrawShape:

    @staticmethod
    def square(x):
        for i in range(x):
            output = ''
            for j in range(x):
                output += '*'
            print(output)

    @staticmethod
    def empty_square(x):
        for i in range(x):
            output = ''
            for j in range(x):
                if j == 0 or j == x-1 or i == 0 or i == x-1:
                    output += '*'
                else:
                    output += ' '
            print(output)


def run():
    DrawShape.empty_square(5)
