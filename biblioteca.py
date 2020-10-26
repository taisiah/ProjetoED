'''Guia de Estilo
1 - Separe funções e definições de classe com duas linhas em branco
2 - identificadores de variaveis: "minúsculas_separadas_com_underscore"
3 - nomes de funções: PalavrasComeçandoPorMaiúscula'''

#funcionaro => nome, login, senha, e-mail
lista_funcionarios = []
funcionario = ['Administrador','admin','123','admin@iesp.com']
lista_funcionarios.append(funcionario)
logado = False

def login (login,senha):
    for f in lista_funcionarios:
        if f[1] == login and f[2] == senha:
            return f[0]
    return None


'''def cadastro_livro():
    código =
    livro=[]
    titulo=input(" titulo do livro:")
    autor=input(" autor :")
    ano=int(input(" ano :"))
    editora=input(" editora :")
    edicao=input(" edição :")
    quantidade= int(input("Digite uma quantidade de exemplares:"))

    print("Livro cadastrado com sucesso!")


def remove_livro():

    print("Título removido com sucesso!")

def status():

def buscar():
    busca = input("Digite nome para busca")
    if 'busca' ==

def relatorio():
'''
def main():
    print("Bem vindo a Morais Library")
    while True:
        login_func = input("Digite seu login: ")
        senha_func = input("Digite sua senha: ")
        nome = login (login_func,senha_func)
        if nome == None:
            print("Login ou senha inválido, digite novamente.")
        else:
            print("Bem vindo,",nome)
            break

if __name__ == "__main__":
    main()