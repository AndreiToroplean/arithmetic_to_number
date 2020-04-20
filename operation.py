class Operation:
    def __init__(self, operation, symbol):
        assert callable(operation), "operation should be callable."
        self.operation = operation
        self.symbol = symbol

    def get_phrase(self, phrase_a, phrase_b):
        return f"({phrase_a} {self.symbol} {phrase_b})"

    def get_value(self, value_a, value_b):
        return self.operation(value_a, value_b)
