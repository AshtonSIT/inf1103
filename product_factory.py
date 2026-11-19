from product import Product, PhysicalProduct, DigitalProduct
from supplier import Supplier


class ProductFactory:
    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float,
               stock_quantity: int, supplier: Supplier, extra: float = 1.0) -> Product:
        #extra is the weight (kg) for a physical product, or the file size (MB) for a digital product
        if product_type == "physical":
            return PhysicalProduct(product_id, name, price, stock_quantity, extra, supplier)
        elif product_type == "digital":
            return DigitalProduct(product_id, name, price, stock_quantity, extra, supplier)
        else:
            raise ValueError(f"Unknown product type: {product_type}")