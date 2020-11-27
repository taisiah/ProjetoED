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
    global categorias
    global tematicas
    print("\n=-=-=-=-=-= ADICIONAR CATEGORIA =-=-=-=-=-=\n")
    arquivo_categorias = open("arqcategorias.txt",'w')
    categoria = input("Digite o nome da categoria que deseja cadastrar: ").upper()
    if categoria in categorias :
        print("Categoria existente")
    else:
        categorias.append(categoria)
        print("Categoria adicionada com sucesso!")
        categorias.sort()
        saida = []
        for e in categorias:
            saida.append(e+"\n")
        arquivo_categorias.writelines(saida)


def cadastro_tematica ():
    print("\n=-=-=-=-=-= ADICIONAR TEMÁTICA =-=-=-=-=-=\n")
    arquivo_tematicas = open("arqtematicas.txt", 'w')
    tematica = input("Digite o nome da temática que deseja cadastrar: ").upper()
    if tematica in tematicas :
        print("Temática existente")
    else:
        tematicas.append(tematica)
        print("Temática adicionada com sucesso!")
        tematicas.sort()
        saida = []
        for e in tematicas:
            saida.append(e + "\n")
        arquivo_tematicas.writelines(saida)


def cadastro_livro():
    global tematicas
    global categorias
    
    print("\n=-=-=-=-=-= CADASTRAR NOVO LIVRO =-=-=-=-=-=\n")
    arquivo_acervo= open("acervo.txt", 'w')

    livro = {
        'titulo':input("Título....: ").upper(),
        'autor':input("Autor.....: "),
        'ano':int(input("Ano.......: ")),
        'editora':input("Editora...: "),
        'edicao':input("Edição....: "),
        'quantidade':int(input("Quantidade: ")),
        'assunto':input("Assunto...: "),
        'reserva': False
    }

    print(' Categorias: ')
    for i in range (0, len(categorias)):
        print (f' [{i+1} - {categorias[i]}]')
    posicao = int(input('Informe o codigo da categoria do livro: '))-1
    print(categorias)
    livro ['categoria'] = categorias[posicao]

    print(' Temáticas: ')
    for i in range (0, len(tematicas)):
        print (f' [{i+1} - {tematicas[i]}]')
    posicao = int(input('Informe o codigo da temática do livro: '))-1
    livro ['tematica'] = tematicas[posicao]

    lista_livros.append(livro)

    saida = []
    for e in lista_livros:
        saida.append(e['titulo'] +" " + e['autor'] + " "+ str(e['ano']) + " "+ e['editora'] + " " + e['edicao'] + " "+ str(e ['quantidade'])+" "+e['assunto']+" "+ str(e['reserva']) +"\n")
    arquivo_acervo.writelines(saida)

    print("Livro cadastrado com sucesso!")
    

def habilita_reserva(tituloLivro):
    global lista_livros
    
    print("\n=-=-=-=-=-= HABILITAR RESERVA DE LIVRO =-=-=-=-=-=\n")

    reservar = input('Disponibilizar livro para reserva [S/N]? ')

    for i in range (0, len(lista_livros)):
        if (lista_livros[i]['titulo']) == tituloLivro:
            if reservar in 'Ss':
                lista_livros[i]['status'] = True
                print(f"Informação atualizada! Livro {tituloLivro} disponível para reserva.")
            else:
                lista_livros[i]['status'] = False
                print(f"Informação atualizada! Livro {tituloLivro} indisponível para reserva.")
            break
   

def ajusta_acervo(tituloLivro):
    global lista_livros

    print("\n=-=-=-=-=-= AJUSTAR ESTOQUE DO ACERVO =-=-=-=-=-=\n")

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

    print("\n=-=-=-=-=-= REMOVER LIVRO =-=-=-=-=-=\n")

    for i in range (0, len(lista_livros)):
        if (lista_livros[i]['titulo']) == tituloLivro:
            print (lista_livros[i])
            lista_livros.pop(i)
            break

    print(f"Livro {tituloLivro} removido com sucesso!")


def busca_livro():
    global lista_livros

    print("\n=-=-=-=-=-=-=-= BUSCAR LIVRO =-=-=-=-=-=-=-=\n")

    filtro = int(input('[1] Título - [2] Autor - [3] Ano - [4] Assunto \nInforme o filtro a ser utilizado na busca: '))
    
    if filtro == 1:
        informacao_busca = input('Informe o TÍTULO do livro: ')
        for i in range (0, len(lista_livros)):
            if (lista_livros[i]['titulo']) == informacao_busca:
                print (f"\nTítulo....: {lista_livros[i]['titulo']}")
                print (f"Autor.....: {lista_livros[i]['autor']}")
                print (f"Ano.......: {lista_livros[i]['ano']}")
                print (f"Editora...: {lista_livros[i]['editora']}")
                print (f"Assunto...: {lista_livros[i]['assunto']}")
                print (f"Categoria.: {lista_livros[i]['categoria']}")
                print (f"Temática..: {lista_livros[i]['tematica']}")
                print (f"Reserva...: {lista_livros[i]['reserva']}")
                

    elif filtro == 2:
        informacao_busca = input('Informe o AUTOR do livro: ')
        for i in range (0, len(lista_livros)):
            if (lista_livros[i]['autor']) == informacao_busca:
                print (f"\nTítulo....: {lista_livros[i]['titulo']}")
                print (f"Autor.....: {lista_livros[i]['autor']}")
                print (f"Ano.......: {lista_livros[i]['ano']}")
                print (f"Editora...: {lista_livros[i]['editora']}")
                print (f"Assunto...: {lista_livros[i]['assunto']}")
                print (f"Categoria.: {lista_livros[i]['categoria']}")
                print (f"Temática..: {lista_livros[i]['tematica']}")
                print (f"Reserva...: {lista_livros[i]['reserva']}")
                

    elif filtro == 3:
        informacao_busca = input('Informe o ANO do livro: ')
        for i in range (0, len(lista_livros)):
            if (lista_livros[i]['ano']) == informacao_busca:
                print (f"\nTítulo....: {lista_livros[i]['titulo']}")
                print (f"Autor.....: {lista_livros[i]['autor']}")
                print (f"Ano.......: {lista_livros[i]['ano']}")
                print (f"Editora...: {lista_livros[i]['editora']}")
                print (f"Assunto...: {lista_livros[i]['assunto']}")
                print (f"Categoria.: {lista_livros[i]['categoria']}")
                print (f"Temática..: {lista_livros[i]['tematica']}")
                print (f"Reserva...: {lista_livros[i]['reserva']}")
                

    elif filtro == 4:
        informacao_busca = input('Informe o ASSUNTO do livro: ')
        for i in range (0, len(lista_livros)):
            if (lista_livros[i]['assunto']) == informacao_busca:
                print (f"\nTítulo....: {lista_livros[i]['titulo']}")
                print (f"Autor.....: {lista_livros[i]['autor']}")
                print (f"Ano.......: {lista_livros[i]['ano']}")
                print (f"Editora...: {lista_livros[i]['editora']}")
                print (f"Assunto...: {lista_livros[i]['assunto']}")
                print (f"Categoria.: {lista_livros[i]['categoria']}")
                print (f"Temática..: {lista_livros[i]['tematica']}")
                print (f"Reserva...: {lista_livros[i]['reserva']}")
                
    else:
        print('Opção Inválida!')


def repete_funcao(funcao):
    continua = 'S'
    while continua in 'Ss':
        funcao()
        continua = input('Fazer novo cadastro [S/N]? ')


def importa_dados(import_arquivo):
    importar = open(import_arquivo,"r")
    print(importar.readlines())

def import_inicial():
    global categorias
    global tematicas
    global lista_livros
    importa_cat = open("arqcategorias.txt","r")
    while True:
        linha = importa_cat.readline()
        if(linha == ""):
            break
        categorias.append(linha)
    importa_tem = open("arqtematicas.txt", "r")
    while True:
        linha = importa_tem.readline()
        if(linha == ""):
            break
        tematicas.append(linha)
    importa_liv = open("acervo.txt", "r")
    while True:
        linha = importa_liv.readline()
        if(linha == ""):
            break
        lista_livros.append(linha)
    #importa_fun = open("listafunc.txt","r")
    


def relatorios():
    tipo_relatorio = input("Digite C para relatórios sobre categorias,T para temáticas e A para acervo")
    if tipo_relatorio == "C" or "c":
        arquivo_categorias = open("relatorio_categorias.txt","r")
        #qtd por categorias / lista das categorias
        print(arquivo_categorias.readlines())
    if tipo_relatorio == "T" or "t":
        arquivo_tematicas = open("relatorio_tematicas.txt","r")
        print(arquivo_tematicas.readlines())
        # qtd por categorias / lista das categorias
    if tipo_relatorio == "a" or "A":
        arquivo_acervo = open("relatorio_acervo.txt","r")
        print(arquivo_acervo.readlines())
        # qtd por categorias / lista das categorias
    else:
        print("Relatório não identificado")



def status():
    informacao_busca = input('Informe o TÍTULO do livro: ')
    for i in range (0, len(lista_livros)):
        if (lista_livros[i]['titulo']) == informacao_busca:
            if {lista_livros[i]['reserva']}  == True :
                print (f"\nTítulo....: {lista_livros[i]['titulo']}")
                print (f"Categoria.: {lista_livros[i]['categoria']}")
                print (f"Temática..: {lista_livros[i]['tematica']}")
            else:
                print("Data de devolução prevista",data)
        else:
            print("Título não encontrado!")



def menu():
    print("\n=-=-=-=-=-=-=-= MENU PRINCIPAL =-=-=-=-=-=-=-=\n")
    
    print("    1  - CADASTRAR CATEGORIA ")
    print("    2  - CADASTRAR TEMÁTICA")
    print("    3  - CADASTRAR LIVRO")
    print("    4  - HABILITAR RESERVA")
    print("    5  - ATUALIZAR QUANTIDADE DE EXEMPLARES")
    print("    6  - REMOVER TÍTULO")
    print("    7  - BUSCAR LIVRO")
    print("    8  - IMPORTAR DADOS")
    print("    9  - RELATÓRIOS")
    print("    10 - STATUS DO LIVRO")
    print("    11 - Sair ")

    return input("\nDigite a opção desejada: ")


def main():
    print("\n=-=-=-=-=-= MORAIS LIBRARY - Sistema de Gestão Bibliotecária =-=-=-=-=-=\n")
    tentativas = 0
    import_inicial()
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
                opcao = menu()
                if opcao == '1':
                    repete_funcao(lambda: cadastro_categoria())
                elif opcao == '2':
                    repete_funcao(lambda: cadastro_tematica())
                elif opcao == '3':
                    repete_funcao(lambda: cadastro_livro())
                elif opcao == '4':
                    habilita_reserva(input('Titulo do livro para alterar disponibilização reserva: ').upper())
                elif opcao == '5':
                    ajusta_acervo(input('Titulo do livro deseja ajustar o acervo: ').upper())
                elif opcao == '6':
                    remove_livro(input('Titulo do livro deseja remover: ').upper())
                elif opcao == '7':
                    busca_livro()
                elif opcao == '8':
                    import_arquivo = input("Digite o arquivo que deseja importar")
                    importa_dados(import_arquivo +".txt")
                elif opcao == '9':
                    relatorios()
                elif opcao == '10':
                    status()
                elif opcao == '11':
                    break
                else:
                    print("Opção inválida")



if __name__ == "__main__":
    main()