from operation import Operation
from arithmetic_beast import ArithmeticBeast


def main():
    addition = Operation(lambda a, b: a+b, '+')
    subtraction = Operation(lambda a, b: a-b, '-')
    multiplication = Operation(lambda a, b: a*b, '*')
    division = Operation(lambda a, b: a/b, '/')

    numbers = [25, 75, 4, 100]
    operations = [addition, subtraction, multiplication]
    expected_result = 425

    beast = ArithmeticBeast(numbers, operations)
    beast.print_phrases_for_result(expected_result)


if __name__ == '__main__':
    main()
