from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('Selecione uma opção a baixo:')
    print('1 - Cadastrar produto')
    print('2 - Listar produtos')
    print('3 - Comrpar produto')
    print('4 - Visualizar carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair do sistema')

    opcao:int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Falow otario!')
        sleep(2)
        exit()
    else:
        print('Opção invalida')
        sleep(2)
        menu()


def cadastrar_produto() -> None:
    print('Cadastro de produto')

    nome: str = str(input('Nome do produto: '))
    preco: float = float(input('Preco do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'Produto{produto.nome} foi cadastrado com sucesso')

    sleep(2)
    menu()

def listar_produtos() -> None:
    if len(produtos) > 0:
        print('Listando produtos:\n')
        for produto in produtos:
            print(produto)
            print('----------------')
            sleep(1)
    else:
        print('Ainda não existem produtos cadastrados.')
    sleep(2)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o código do produto que deseja adicionar nao carrinho: ')
        print('---------------------------------------------------------------')
        print('====================Produtos Disponiveis=======================')
        for produto in produtos:
            print(produto)
            print('---------------------------------------------------------------')
            sleep(1)
        codigo: int = int(input())

        produto: Produto = pegar_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quantidade: item = item.get(produto)
                    if quantidade:
                        item[produto] = quantidade + 1
                        print(f'O produto {produto.nome} agora tem no carrinho {quantidade + 1} unidade(s)')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado no carrinho')
                    sleep(2)
                    menu()

            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu()
        else:
            print(f'O produto com o codigo {codigo} nnão foi encontrado')
            sleep(2)
            menu()

    else:
        print('Ainda não existem produtos para vender')
    sleep(2)
    menu()

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        total_carrinho: float = 0
        total_item: float = 0
        print('Carrinho')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(dados[1])
                total_item += dados[0].preco * dados[1]
                print(f'total:{formata_float_str_moeda(total_item)}')
                print('-----------------')
        total_carrinho += total_item
        print('----------------')
        print(f'Total do carrinho: {formata_float_str_moeda(total_carrinho)}')
        carrinho.clear()
        sleep(5)


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        total_carrinho: float = 0
        total_do_item: float = 0
        print('Carrinho')

        for item in carrinho:
            total_item: float = 0
            for dados in item.items():
                total_item += dados[0].preco * dados[1]
                print(f'{dados[0]}  Quantidade{dados[1]} Total:{formata_float_str_moeda(total_item)}')
                print('-----------------')
            total_do_item += total_item
        total_carrinho += total_do_item
        print('----------------')
        print(f'Total do carrinho: {formata_float_str_moeda(total_carrinho)}')
        sleep(5)

    else:
        print('Carrinho vazio')
    sleep(2)
    menu()


def pegar_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p

if __name__ == '__main__':
    main()
