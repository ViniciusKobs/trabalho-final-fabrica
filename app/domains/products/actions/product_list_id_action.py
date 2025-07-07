from app.domains.products.dtos.products_dto import ProductsDTO
from app.models.products_model import ProductsModel


def productListIdAction(request):

    product = ProductsModel.listId(request.getProductId())
    return ProductsDTO(model=product)