import os

class Cliente:
    def __init__(self, nome, razao_social, cnpj, inscricao_estadual, endereco, telefone, email ):
        self.nome = nome
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.inscricao_estadual = inscricao_estadual
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
                
class Produto:
    def __init__(self, codProduto, nome, preco):
        self.codProduto = codProduto
        self.nome = nome
        self.preco = preco

class Pedido:
    def __init__(self, numPedido, codProduto, codCliente, quantidade, totalPedido, dataPedido):
        self.numPedido = numPedido
        self.codProduto = codProduto
        self.codCliente = codCliente
        self.quantidade = quantidade
        self.totalPedido = totalPedido
        self.dataPedido = dataPedido
        
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
    
    def encontraProduto(self, dadoProduto):
        atual = self.primeiro
 #       encontrado = False
        if self.primeiro is None:
            print("Lista vazia!")
            return
        
        while atual:
            if dadoProduto == atual.produto.codProduto or dadoProduto == atual.produto.nome:
                print("Produto encontrado")
                print("Nome:", atual.produto.nome, "Codigo:",atual.produto.codProduto, "Preço:",atual.produto.preco)
 #               encontrado = True
                return
            atual = atual.proximo
 #       if not encontrado:
        print("Produto não registrado")
        return
    
    def removeProduto(self, codProduto):
        if self.primeiro is None:
            print("Lista vazia!")
            return
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
        if self.primeiro is None:
            print("Lista vazia!")
            return
        
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

def criaCliente():
        nome = input("Nome:")
        razao_social = input("Razão social:")
        cnpj = input("Cnpj:")
        inscricao_estadual = input("Inscrição estadual:")
        endereco = input("Endereço:")
        telefone = input("Telefone:")
        email = input("Email:")
        cliente = Cliente(nome, razao_social, cnpj, inscricao_estadual, endereco, telefone, email)
        return cliente

def criaProduto():
        codigo = input("Insira o codigo do produto:")
        nome = input("Insira o nome do produto:")
        preco = input("Insira o preço do produto:")
        produto = Produto(codigo, nome, preco)
        return produto


#MENU 
listaCliente = []
listaProdutos = ListaProdutos()

while True:
    #os.system("clear")
    print("1-Encontre o produto\n2-Inserir o produto\n3-Remover o produto\n4-Modificar algum produto\n"
      "5-Listar todos os produtos\n6-Gerar o cliente\n7-Processar venda\n8-Listar os dados do cliente\n0-Encerrar")
    option = int(input("Qual a sua opção:"))
    match option:
        case 1:
            os.system("clear")
            dado = input("Opção 1 escolhida, insira o produto a ser exibido: ")
            listaProdutos.encontraProduto(dado)
        case 2:
            os.system("clear")
            print("Opção 2 escolhida, cadastrando as informações do produto: ")
            listaProdutos.adicionarOrdenado(criaProduto())
        case 3:
            os.system("clear")
            dado = input("Opção 3 escolhida, insira o codigo do produto a ser removido: ")
            listaProdutos.removeProduto(dado)
        case 4:
            os.system("clear")
            dado = input("Opção 4 escolhida, insira o codigo do produto a ser modificado: ")
            listaProdutos.alteraProduto(dado)
        case 5:
            os.system("clear")
            print("Opção 5 escolhida, listando os produtos\n")
            listaProdutos.imprimir()
        case 6:
            os.system("clear")
            print("Opção 6 escolhida, gerando o cliente\n")
            listaCliente.append(criaCliente())
#            for cliente in listaCliente:
#                print(cliente.nome, cliente.razao_social, cliente.inscricao_estadual, cliente.endereco, cliente.telefone, cliente.email)
        case 7:
            os.system("clear")
            print("Opção 7 escolhida, insira as informações da venda:")
        case 8:
            os.system("clear")
            print("Opção 8 escolhida, insira o nome do cliente a ser exibido:")
        case 0:
            os.system("clear")
            print("Encerrando")
            break
        case _:
            os.system("clear")
            print("Comando inexistente, insira novamente\n") 