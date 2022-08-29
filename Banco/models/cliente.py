from datetime import date
from utils.helper import date_para_str, str_para_date

class Cliente:
    contador: int =101

    def __init__(self: object, nome: str, email: str, cpf: str, data_nasc: str) -> None:
        self.__codigo: int = Cliente.contador
        self.__nome: str = nome
        self.__email: str = email
        self.__cpf: str = cpf
        self.__data_nasc: date = str_para_date(data_nasc)
        self.__cadastro: date = date.today()
        Cliente.contador += 1

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def email(self) -> str:
        return self.__email

    @property
    def cpf(self) -> int:
        return self.__cpf

    @property
    def data_nasc(self) -> str:
        return date_para_str(self.__data_nasc)

    @property
    def cadastro(self) -> str:
        return date_para_str(self.__cadastro)

    def __str__(self) -> str:
        return f'Codigo: {self.codigo}   Nome: {self.nome}   Email: {self.email}   Cpf: {self.cpf}   Data nasc: {self.data_nasc}   cadastro: {self.cadastro}'
