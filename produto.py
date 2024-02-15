class Produto:
    def __init__(self, codProduto, nome, preco):
        self.codProduto = codProduto
        self.nome = nome
        self.preco = preco
class No:
    def __init__(self, produto):
        self.produto = produto
        self.proximo = None

class ListaProdutos:
    def __init__(self):
        self.primeiro = None

    def imprimirLista(self):
        atual = self.primeiro
        while atual:
            print("Codigo:", atual.produto.codProduto)
            print("Nome:", atual.produto.nome)
            print("Valor: R$:", atual.produto.preco)
            print("\n")
            atual = atual.proximo
        return
    
    def listaVazia(self):
        if self.primeiro is None:
            print("Lista vazia!")
            return True
        
    def adicionarOrdenado(self, prod):
        novo_no = No(prod)
        encontrado = False

        if self.primeiro is None:
            self.primeiro = novo_no
        elif prod.codProduto <= self.primeiro.produto.codProduto:
            novo_no.proximo = self.primeiro
            self.primeiro = novo_no

        else:
            atual = self.primeiro
            while atual.proximo and atual.proximo.produto.codProduto < prod.codProduto:
                if atual.produto.codProduto == prod.codProduto:
                    encontrado = True
                    break
                atual = atual.proximo
            
            if not encontrado:
                novo_no.proximo = atual.proximo
                atual.proximo = novo_no
            else:
                print("Já existente na lista")
    
    def retornaProduto(self, codProduto):
        if self.listaVazia():return 

        atual = self.primeiro
        while atual:
            if codProduto == atual.produto.codProduto:
                return atual.produto
            atual = atual.proximo
        return

    def encontraProduto(self, dadoProduto):
        if self.listaVazia():return

        atual = self.primeiro
        while atual:
            if dadoProduto == atual.produto.codProduto or dadoProduto == atual.produto.nome:
                print("Produto encontrado!")
                print("Nome:", atual.produto.nome, "Codigo:",atual.produto.codProduto, "Preço:",atual.produto.preco)
                return
            atual = atual.proximo
        print("Produto não registrado")
        return
    
    def removeProduto(self, codProduto):
        if self.listaVazia():return

        if self.primeiro.produto.codProduto == codProduto:
            temp = self.primeiro
            self.primeiro = self.primeiro.proximo
            del temp
            print("Elemento removido")
            return
        
        atual = self.primeiro
        while atual.proximo:
            if atual.proximo.produto.codProduto == codProduto:
                    temp = atual.proximo
                    atual.proximo = atual.proximo.proximo
                    del temp
                    print("Elemento removido")
            atual = atual.proximo
        print("Produto não encontrado")
        return
    
    def alteraProduto(self, codProduto):
        if self.listaVazia():return

        atual = self.primeiro
        while atual:
            if codProduto == atual.produto.codProduto:
                print("Produto encontrado, alterando ele\n")
                nome = input("Insira o nome:")
                preco = input("Insira o preco do produto:")
                atual.produto.nome = nome
                atual.produto.preco = preco
                print("Nome:", atual.produto.nome, "Codigo:",atual.produto.codProduto, "Preço:",atual.produto.preco)
                return
            atual = atual.proximo
        return
    
def criaProduto():
    codigo = int(input("Insira o codigo do produto:"))
    nome = input("Insira o nome do produto:")
    preco = float(input("Insira o preço do produto:"))
    prod = Produto(codigo,nome,preco)
    return prod