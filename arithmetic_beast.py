import itertools


class ArithmeticBeast:
    def __init__(self, numbers, operations):
        self.numbers = numbers
        self.operations = operations
        self.trees = self._make_all_trees()
        self.results = self._compute_all()

    @classmethod
    def _make_tree(cls, numbers_p, split_p, level=0, shift=0):
        if len(numbers_p) == 1:
            return numbers_p[0]

        while True:
            split = split_p[level] - shift
            if 0 < split < len(numbers_p):
                break
            level += 1

        part_a = cls._make_tree(numbers_p[:split], split_p, level + 1, shift)
        part_b = cls._make_tree(numbers_p[split:], split_p, level + 1, shift + split)
        return part_a, part_b

    @classmethod
    def _compute(cls, tree, operations_p, level=0):
        values = []
        phrases = []
        for subtree in tree:
            try:
                value, phrase = cls._compute(subtree, operations_p, level + 1)
            except TypeError:
                values.append(subtree)
                phrases.append(f"{subtree}")
            else:
                values.append(value)
                phrases.append(phrase)

        operation = operations_p.pop()
        try:
            value = operation.get_value(*values)
        except ZeroDivisionError:
            value = float("NaN")
        phrase = operation.get_phrase(*phrases)
        return value, phrase

    def _make_all_trees(self):
        # todo: make it generate unique trees by default, removing the need to use a set.
        #   I think I need to code a function replacing itertools.permutations here to achieve that.

        numbers_ps = list(itertools.permutations(self.numbers))

        trees = set()
        for split_p in itertools.permutations(range(1, len(self.numbers))):
            for numbers_p in numbers_ps:
                trees.add(self._make_tree(numbers_p, split_p))
        return trees

    def _compute_all(self):
        operations_ps = list(itertools.permutations(self.operations))

        for tree in self.trees:
            for operations_p in operations_ps:
                operations_p = list(operations_p)  # self._compute requires it to be mutable.
                yield self._compute(tree, operations_p)

    def print_phrases_for_result(self, expected_result):
        for result in self.results:
            if result[0] == expected_result:
                print(f"{result[1]} = {result[0]}")
