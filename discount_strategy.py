from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        pass

class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float) -> None:
        self.percentage: float = percentage

    def apply(self, total: float) -> float:
        return total * (1 - self.percentage / 100)

class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: float, amount: float) -> None:
        self.threshold: float = threshold
        self.amount: float = amount

    def apply(self, total: float) -> float:
        return total - self.amount if total >= self.threshold else total

class StudentDiscount(DiscountStrategy):
    #Fourth strategy: 5% off. Order does not change to support this
    def apply(self, total: float) -> float:
        return total * 0.95