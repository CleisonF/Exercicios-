class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade


    def exibir(self):
        return f'Produto: {self.nome} - Preço: R$ {self.preco} - Quantidade: {self.quantidade}'


class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        print(f'Produtos no estoque: ')
        print()
        for produto in self.produtos:
            print(produto.exibir())


    def buscar_produto(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                print(produto.exibir())
                return
        print('Produto não encontrado')

    def valor_total_estoque(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco * produto.quantidade
        return round(total, 2)

    def vender_produto(self, nome, quantidade):
        for produto in self.produtos:
            if produto.nome == nome:
                if produto.quantidade >= quantidade:
                    produto.quantidade -= quantidade
                    total = round(produto.preco * quantidade, 2)
                    print(f'Venda realizada: {quantidade} x {produto.nome} por R$ {total}')
                else:
                    print(f'Estoque insuficiente para {produto.nome}. Disponivel {produto.quantidade}')
                    break
                return
        else:
            print(f'Produto {nome} não encontrado no estoque.')




p1 = Produto('Arroz', 5.99, 20)
p2 = Produto('Feijão', 7.50, 10)
estoque = Estoque()
estoque.adicionar_produto(p1)
estoque.adicionar_produto(p2)
estoque.listar_produtos()
estoque.vender_produto('Feijão', 5)
estoque.vender_produto('Macarrão', 2)
print('O valor do estoque: R$',estoque.valor_total_estoque())