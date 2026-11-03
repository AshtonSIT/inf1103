from abc import ABC, abstractmethod

#4.1 Create a CanBeShipped interface with calculate_shipping_cost method
class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self) -> float:
        pass

#3.1 Convert Product into an abstract class
class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        self._product_id = product_id
        self._name = name
        self._price = float(price)
        self._stock = int(stock)

    def getID(self) -> str:
        return self._product_id

    def getName(self) -> str:
        return self._name

    def getPrice(self) -> float:
        return self._price

    def getStock(self) -> int:
        return self._stock

    def update_stock(self, new_quantity: int) -> None:
        if new_quantity >= 0:
            self._stock = new_quantity

    def display_information(self) -> None:
        print(
            f"ID: {self._product_id} | Name: {self._name} | "
            f"Price: ${self._price:.2f} | Stock: {self._stock}", 
            end=" "
        )

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        pass

#1.2 Concrete Class for PhysicalProduct
class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float):
        super().__init__(product_id, name, price, stock)
        self._weight = float(weight)

    #weight subclass
    def get_weight(self) -> float:
        return self._weight

    #2.1 & 2.2 Method Overriding (reuse parent logic without code repetition)
    def display_information(self) -> None:
        super().display_information()
        print(f" | Weight: {self._weight:.2f} kg")

    #3.2 Implement the required abstract methods for PhysicalProduct
    def get_fulfilment_info(self) -> str:
        return f"Shipment required. Weight: {self._weight:.2f} kg."

    #4.2 Implement the CanBeShipped interface method for PhysicalProduct
    def calculate_shipping_cost(self) -> float:
        return 5.00 + (self._weight * 2.00)

    def to_dict(self) -> dict:
        return {
            "type": "physical",
            "id": self._product_id,
            "name": self._name,
            "price": self._price,
            "stock": self._stock,
            "weight": self._weight
        }

#1.3 Concrete Class for DigitalProduct
class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, file_size: float):
        super().__init__(product_id, name, price, stock)
        self._file_size = float(file_size)

    def get_file_size(self) -> float:
        return self._file_size

    #2.1 & 2.2 Method Overriding (reuse parent logic without code repetition)
    def display_information(self) -> None:
        super().display_information()
        print(f" | File Size: {self._file_size:.1f} MB")

    #3.2 Implement the required abstract methods for DigitalProduct
    def get_fulfilment_info(self) -> str:
        return f"Digital download available. File size: {self._file_size:.1f} MB."

    def to_dict(self) -> dict:
        return {
            "type": "digital",
            "id": self._product_id,
            "name": self._name,
            "price": self._price,
            "stock": self._stock,
            "file_size": self._file_size
        }