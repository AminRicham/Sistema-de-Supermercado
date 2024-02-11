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

#####VERIFICAR SE JÀ EXISTE
    def adicionarOrdenado(self, produto):
        novo_no = No(produto)
        if self.primeiro is None or produto.codProduto < self.primeiro.produto.codProduto :
            self.primeiro = novo_no
        else:
            atual = self.primeiro
            while atual.proximo and atual.proximo.produto.codProduto < produto.codProduto:
                atual = atual.proximo
            novo_no.proximo = atual.proximo
            atual.proximo = novo_no
        return
    
    def imprimir(self):
        atual = self.primeiro
        while atual:
            print("Codigo:", atual.produto.codProduto)
            print("Nome:", atual.produto.nome)
            print("Valor:", atual.produto.preco)
            print("\n")
            atual = atual.proximo
        return
    
    def listaVazia(self):
        if self.primeiro is None:
            print("Lista vazia!")
            return True
        
    def retornaProduto(self, codProduto):
        atual = self.primeiro
        if self.listaVazia():return
        while atual:
            if codProduto == atual.produto.codProduto:
                return atual.produto
            atual = atual.proximo
        return

    def encontraProduto(self, dadoProduto):
        atual = self.primeiro
        if self.primeiro is None:
            print("Lista vazia")
            return
        while atual:
            if dadoProduto == atual.produto.codProduto or dadoProduto == atual.produto.nome:
                print("Produto encontrado")
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
    #produto = Produto.produto(codigo, nome, preco)
    return prod