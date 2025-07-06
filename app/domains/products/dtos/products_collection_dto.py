from app.domains.products.dtos.products_dto import ProductsDTO

class ProductsCollectionDTO:
    def __init__(
        self,
        collection=None,
        model=None
    ):
        if model is not None:
            collection = [ProductsDTO(model=product) for product in model]
        elif collection is None:
            collection = []

        self.collection = collection

    def toArray(self):
        return [product.toDict() for product in self.collection]
