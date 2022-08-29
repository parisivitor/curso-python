from datetime import date
from datetime import datetime


def date_para_str(data: date) -> str:
    return f'{data.day}/{data.month}/{data.year}'


def str_para_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')


def formata_float_str_moeda(valor: float) -> str:
    return f'R$ {valor:,.2f}'
