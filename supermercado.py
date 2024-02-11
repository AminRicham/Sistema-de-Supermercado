import os
import cliente
import produto
import pedido


#MENU 
listaCliente = []
listaProdutos = produto.ListaProdutos()
listaPedido = []

prod1 = produto.Produto(1, "arroz", 11)
listaProdutos.adicionarOrdenado(prod1)
listaProdutos.adicionarOrdenado(produto.Produto(3, "abacate", 33))
listaProdutos.adicionarOrdenado(produto.Produto(2, "feijão", 22))

listaCliente.append(cliente.Cliente("Amin", "Vida", "123","rj","rua","1234","aminricham@gmailcom"))
listaCliente.append(cliente.Cliente("Adriana", "olhos", "567","sp","travessa","5678","adriana@gmailcom"))
listaCliente.append(cliente.Cliente("Vidal", "jobs", "1011","mg","ap","101112","vidal@gmailcom"))

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
            listaProdutos.adicionarOrdenado(produto.criaProduto())
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
            listaCliente.append(cliente.criaCliente())
#            for cliente in listaCliente:
#                print(cliente.nome, cliente.razao_social, cliente.inscricao_estadual, cliente.endereco, cliente.telefone, cliente.email)
        case 7:
            os.system("clear")
            print("Opção 7 escolhida, gerando o pedido:")
            listaPedido.append(pedido.criaPedido(listaProdutos))
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