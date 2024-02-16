from datetime import date
import produto

class Pedido:
    def __init__(self, numPedido, codProduto, codCliente, quantidade, totalPedido, dataPedido):
        self.numPedido = numPedido
        self.codProduto = codProduto
        self.codCliente = codCliente
        self.quantidade = quantidade
        self.totalPedido = totalPedido
        self.dataPedido = dataPedido

"A função cria um pedido e o relaciona com um cliente"
def criaPedido(listaProdutos):
        
        if listaProdutos.listaVazia():
            return
        listaProdutos.imprimir()

        codProduto = input("Insira o codigo do produto:")
        prod = listaProdutos.retornaProduto

        if prod is None:
            print("Nao encontrado")
            return
        
        numPedido = input("Insira o numero do pedido:")
        codCliente = input("Insira o cnpj do cliente:")
        quantidade = int(input("Insira a quantidade vendida:"))
        dataPedido = date.today()

        totalPedido = float(quantidade) * float(prod.preco)

        return Pedido(numPedido, codProduto, codCliente, quantidade, totalPedido, dataPedido)
