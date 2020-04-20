import itertools


class ArithmeticBeast:
    def __init__(self, numbers, operations):
        self.numbers = numbers
        self.operations = operations
        self.orders = self._make_orders()
        self.results = self._compute_all()

    @staticmethod
    def _make_tree(numbers_p, split_p, level=0, shift=0):
        if len(numbers_p) == 1:
            return numbers_p[0]

        while True:
            split = split_p[level] - shift
            if 0 < split < len(numbers_p):
                break
            level += 1

        part_a = ArithmeticBeast._make_tree(numbers_p[:split], split_p, level + 1, shift)
        part_b = ArithmeticBeast._make_tree(numbers_p[split:], split_p, level + 1, shift + split)
        return part_a, part_b

    @staticmethod
    def _compute(order, operations_p, level=0):
        values = []
        phrases = []
        for part in order:
            try:
                value, phrase = ArithmeticBeast._compute(part, operations_p, level + 1)
            except TypeError:
                values.append(part)
                phrases.append(f"{part}")
            else:
                values.append(value)
                phrases.append(phrase)

        operation = operations_p.pop()
        try:
            value = operation.get_value(*values)
        except ZeroDivisionError:
            value = float("NaN")
        return value, operation.get_phrase(*phrases)

    def _make_orders(self):
        numbers_ps = list(itertools.permutations(self.numbers))

        orders = set()
        for split_p in itertools.permutations(range(1, len(self.numbers))):
            for numbers_p in numbers_ps:
                orders.add(self._make_tree(numbers_p, split_p))
        return orders

    def _compute_all(self):
        operations_ps = list(itertools.permutations(self.operations))

        results = []
        for order in self.orders:
            for operations_p in operations_ps:
                results.append(self._compute(order, list(operations_p)))
        return results

    def check_possible(self, proposition):
        for result in self.results:
            if result[0] == proposition:
                print(f"{result[1]} = {result[0]}")
