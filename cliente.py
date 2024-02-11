class Cliente:
    def __init__(self, nome, razao_social, cnpj, inscricao_estadual, endereco, telefone, email ):
        self.nome = nome
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.inscricao_estadual = inscricao_estadual
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

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
