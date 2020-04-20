from operation import Operation
from arithmetic_beast import ArithmeticBeast


def main():
    addition = Operation(lambda a, b: a+b, '+')
    subtraction = Operation(lambda a, b: a-b, '-')
    multiplication = Operation(lambda a, b: a*b, '*')
    division = Operation(lambda a, b: a/b, '/')

    numbers = [75, 25, 4, 100]
    operations = [addition, subtraction, multiplication]
    proposition = 425

    beast = ArithmeticBeast(numbers, operations)
    beast.check_possible(proposition)


if __name__ == '__main__':
    main()