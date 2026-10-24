class Product:
    def __init__(self, product_id: str, name: str, price:float, stock: int):
        self.__product_id = product_id
        self.__name = name
        self.__price = float(price)
        self.__stock = int(stock)

    def getID(self) -> str:
        return self.__product_id

    def getName(self) -> str:
        return self.__name

    def getPrice(self) -> float:
        return self.__price

    def getStock(self) -> int:
        return self.__stock

    def update_stock(self, new_quantity: int) -> None:
        if new_quantity >= 0:
            self.__stock = new_quantity

    def display_information(self) -> None:
        print(
            f"ID: {self.__product_id} | Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | Stock: {self.__stock}"
        )

    #for JSON serialization
    def to_dict(self) -> dict:
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
        }