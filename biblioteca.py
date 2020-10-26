'''Guia de Estilo
1 - Separe funções e definições de classe com duas linhas em branco
2 - identificadores de variaveis: "minúsculas_separadas_com_underscore"
3 - nomes de funções: PalavrasComeçandoPorMaiúscula'''

#funcionário => nome, login, senha, e-mail
lista_funcionarios = []
funcionario = ['Administrador','admin','123','admin@iesp.com']
lista_funcionarios.append(funcionario)

categorias = []
tematicas = []

#livro => titulo,autor,ano,editora,edicao,quantidade,habilitacao
lista_livros = []


def login (login,senha):
    for f in lista_funcionarios:
        if f[1] == login and f[2] == senha:
            return f[0]
    return None


def cadastro_livro():
    titulo=input(" titulo do livro:")
    autor=input(" autor :")
    ano=int(input(" ano :"))
    editora=input(" editora :")
    edicao=input(" edição :")
    quantidade= int(input("Digite uma quantidade de exemplares:"))
    lista_livros.append([titulo,autor,ano,editora,edicao,quantidade,False])

    print("Livro cadastrado com sucesso!")

'''
def remove_livro():

    print("Título removido com sucesso!")

def status():
    
    if status == True :
        

def buscar():
    busca = input("Digite nome para busca")
    if 'busca' ==

def relatorio():
'''

def print_menu():
    print("Digite a opção desejada: ")
    print("    1 - CADASTRAR CATEGORIA ")
    print("    2 - CADASTRAR TEMÁTICA")
    print("    3 - CADASTRAR LIVRO")
    print("    4 - HABILITAR RESERVA")
    print("    5 - ATUALIZAR QUANTIDADE DE EXEMPLARES")
    print("    6 - REMOVER TÍTULO")
    print("    7 - BUSCA")
    print("    8 - IMPORTAR DADOS")
    print("    9 - RELATÓRIOS")
    print("    10 - STATUS")
    print("    11 - Sair ")

def cadastro_categoria ():
    categoria = input("Digite o nome da categoria que deseja cadastrar: ")
    if categoria in categorias :
        print("Categoria existente")
    else:
        categorias.append(categoria)
        print("Categoria adicionada com sucesso!")
        categorias.sort()
def cadastro_tematica ():
    tematica = input("Digite o nome da temática que deseja cadastrar: ")
    if tematica in tematicas :
        print("Temática existente")
    else:
        tematicas.append(tematica)
        print("Temática adicionada com sucesso!")
        tematicas.sort()





def main():
    print("Bem vindo à Morais Library")
    tentativas = 0
    while True:
        login_func = input("Digite seu login: ")
        senha_func = input("Digite sua senha: ")
        nome = login (login_func,senha_func)
        if nome == None:
            print("Login ou senha inválido, digite novamente.")
            tentativas+=1
            if tentativas >= 3 :
                print ("Esqueceu sua senha? Entre em contato com o administrador.")
                return
        else:
            tentativas=0
            print("Bem vindo,",nome)
            while True:
                print_menu()
                opcao = input()
                if opcao == '1':
                    cadastro_categoria()
                elif opcao == '2':
                    cadastro_tematica()
                elif opcao == '3':
                    cadastro_livro()
                elif opcao == '4':
                    #printar função enquanto não faz
                    print("HABILITAR RESERVA")
                elif opcao == '5':
                    print("ATUALIZAR QUANTIDADE ACERVO")
                elif opcao == '6':
                    print("REMOVER")
                elif opcao == '7':
                    print("BUSCA")
                elif opcao == '8':
                    print("IMPORTAR")
                elif opcao == '9':
                    print("RELATORIO")
                elif opcao == '10':
                    print("STATUS")
                elif opcao == '11':
                    break
                else:
                    print("Opção inválida")



if __name__ == "__main__":
    main()