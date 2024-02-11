from datetime import date

class Pedido:
    def __init__(self, numPedido, codProduto, codCliente, quantidade, totalPedido, dataPedido):
        self.numPedido = numPedido
        self.codProduto = codProduto
        self.codCliente = codCliente
        self.quantidade = quantidade
        self.totalPedido = totalPedido
        self.dataPedido = dataPedido

def criaPedido(listaProdutos):
        if listaProdutos.listaVazia():
            return
        listaProdutos.imprimir()
        codProduto = input("Insira o codigo do produto:")
        prod = listaProdutos.retornaProduto(codProduto)

        if prod is None:
            print("Nao encontrado")
            return
        
        numPedido = input("Insira o numero do pedido:")
        codCliente = input("Insira o cnpj do cliente:")
        quantidade = int(input("Insira a quantidade vendida:"))
        dataPedido = date.today()

        totalPedido = quantidade * prod.preco

        return Pedido(numPedido, codProduto, codCliente, quantidade, totalPedido, dataPedido)
