from app.domains.products.dtos.products_dto import ProductsDTO
from app.models.products_model import ProductsModel

def productsListByIdAction(request):
    product = ProductsModel.listById(request.id)
    return ProductsDTO(model=product)