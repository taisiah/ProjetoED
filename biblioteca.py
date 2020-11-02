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

def cadastro_categoria ():
    print("ADICIONAR CATEGORIA")
    categoria = input("Digite o nome da categoria que deseja cadastrar: ")
    if categoria in categorias :
        print("Categoria existente")
    else:
        categorias.append(categoria)
        print("Categoria adicionada com sucesso!")
        categorias.sort()


def cadastro_tematica ():
    print("ADICIONAR TEMÁTICA")
    tematica = input("Digite o nome da temática que deseja cadastrar: ")
    if tematica in tematicas :
        print("Temática existente")
    else:
        tematicas.append(tematica)
        print("Temática adicionada com sucesso!")
        tematicas.sort()


def cadastro_livro():
    print("\nCADASTRO DE LIVRO")
    livro = {
    'titulo':input(" Título....: ").upper(),
    'autor':input(" Autor.....: "),
    'ano':int(input(" Ano.......: ")),
    'editora':input(" Editora...: "),
    'edicao':input(" Edição....: "),
    'quantidade':int(input(" Quantidade: ")),
    'status':False
    }
    lista_livros.append(livro)

    print("Livro cadastrado com sucesso!")
    

def ajusta_acervo(tituloLivro):
    global lista_livros
    global livro
    print("\nAJUSTAR ESTOQUE DO ACERVO")

    for i in range (0, len(lista_livros)):
        if (lista_livros[i]['titulo']) == tituloLivro:
            print(f'Livro: {lista_livros[i]["titulo"]}')
            print(f'Estoque: {lista_livros[i]["quantidade"]} un')
            lista_livros[i]['quantidade'] = int(input('Digite a nova quantidade em estoque: '))
            break

    print('\nQuantidade de exemplares ajustada com sucesso!') 
    print(f'A nova quantidade de acervo do livro {lista_livros[i]["titulo"]} é {lista_livros[i]["quantidade"]} un') 


def remove_livro(tituloLivro):
    global lista_livros
    print("\nREMOVER LIVRO")

    for i in range (0, len(lista_livros)):
        if (lista_livros[i]['titulo']) == tituloLivro:
            print (lista_livros[i])
            lista_livros.pop(i)
            break

    print(f"Livro {tituloLivro} removido com sucesso!")


def busca_livro(tituloLivro):
    global lista_livros
    global livro

    for i in range (0, len(lista_livros)):
        if (lista_livros[i]['titulo']) == tituloLivro:
            print (f"Título...: {lista_livros[i]['titulo']}")
            print (f"Autor....: {lista_livros[i]['autor']}")
            print (f"Ano......: {lista_livros[i]['ano']}")
            print (f"Editora..: {lista_livros[i]['editora']}")
            break

def repete_funcao(funcao):
    continua = 'S'
    while continua in 'Ss':
        funcao()
        continua = input('Fazer novo cadastro [S/N]? ')


'''
def status():
    if status == True :
def relatorio():
'''


def menu():
    print("\n=-=-=-=-=-=-=-= MENU PRINCIPAL =-=-=-=-=-=-=-=")
    
    print("\n    1 - CADASTRAR CATEGORIA ")
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

    return input("\nDigite a opção desejada: ")


def main():
    print("\n=-=-=-=-=-= MORAIS LIBRARY - Sistema de Gestão Bibliotecária =-=-=-=-=-=")
    tentativas = 0
    
    while True:
        login_func = input("\nDigite seu login: ")
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
                opcao = menu()
                if opcao == '1':
                    repete_funcao(lambda: cadastro_categoria())
                elif opcao == '2':
                    repete_funcao(lambda: cadastro_tematica())
                elif opcao == '3':
                    repete_funcao(lambda: cadastro_livro())
                elif opcao == '4':
                    #printar função enquanto não faz
                    print("HABILITAR RESERVA")
                elif opcao == '5':
                    ajusta_acervo(input('Titulo do livro deseja ajustar o acervo: ').upper())
                elif opcao == '6':
                    remove_livro(input('Titulo do livro deseja remover: ').upper())
                elif opcao == '7':
                    busca_livro(input('Titulo do livro deseja pesquisar: ').upper())
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