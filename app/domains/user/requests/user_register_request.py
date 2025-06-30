from app.domains.user.dtos.user_dto import UserDTO
from app.http.request import Request

class UserRegisterRequest(Request):
    def validate(self):
        # TODO: fazer validação de dados
        pass

    def toDtoOrFail(self):
        # TODO: retornar DTO da request, se for invalido falhar
        return UserDTO(username = 'joaogames', email = 'joao@gmail.com', password = 'joaozinho')