from app.domains.products.dtos.products_collection_dto import ProductsCollectionDTO
from app.models.products_model import ProductsModel

def productsListAction(request):
    model = ProductsModel.list(request)
    return ProductsCollectionDTO(model=model)