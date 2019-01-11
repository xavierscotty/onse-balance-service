

class BalanceCalculator:
    def __init__(self, available_balance):
        self.available = available_balance

    def calculate(self, delta):
        return self.available + delta
