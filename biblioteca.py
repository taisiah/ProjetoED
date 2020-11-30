'''Guia de Estilo
1 - Separe funções e definições de classe com duas linhas em branco
2 - identificadores de variaveis: "minúsculas_separadas_com_underscore"
3 - nomes de funções: PalavrasComeçandoPorMaiúscula'''

from datetime import date
data_atual = date.today()

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
        for e in categorias:
            arquivo_categorias.write(e+"\n")
    arquivo_categorias.close()

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
        for e in tematicas:
            arquivo_tematicas.write(e+"\n")
    arquivo_tematicas.close()

def cadastro_livro():
    global tematicas
    global categorias
    global lista_livros

    print("\n=-=-=-=-=-= CADASTRAR NOVO LIVRO =-=-=-=-=-=\n")
    arquivo_acervo= open("acervo.txt", 'w')

    livro = {
        'titulo':input("Título....: ").upper(),
        'autor':input("Autor.....: ").upper(),
        'ano':int(input("Ano.......: ")),
        'editora':input("Editora...: ").upper(),
        'edicao':input("Edição....: "),
        'quantidade':int(input("Quantidade: ")),
        'assunto':input("Assunto...: ").upper(),
        'reserva': False,
        'status': False
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
    for e in lista_livros:
        arquivo_acervo.write(e['titulo']+"\n")
        arquivo_acervo.write(e['autor'] + "\n")
        arquivo_acervo.write(str(e['ano']) + "\n")
        arquivo_acervo.write(e['editora'] + "\n")
        arquivo_acervo.write(e['edicao'] + "\n")
        arquivo_acervo.write(str(e ['quantidade'])+"\n")
        arquivo_acervo.write(e['assunto']+"\n")
        arquivo_acervo.write(str(e['reserva']) + "\n")
        arquivo_acervo.write(str(e['categoria']) + "\n")
        arquivo_acervo.write(str(e['tematica'])+"\n")
        arquivo_acervo.write(str(e['status']) + "\n")

    print("Livro cadastrado com sucesso!")
    arquivo_acervo.close()

def habilita_reserva(tituloLivro):
    global lista_livros
    
    print("\n=-=-=-=-=-= HABILITAR RESERVA DE LIVRO =-=-=-=-=-=\n")

    reservar = input('Disponibilizar livro para reserva [S/N]? ')

    for i in range (0, len(lista_livros)):
        if (lista_livros[i]['titulo']) == tituloLivro:
            if reservar in 'Ss':
                lista_livros[i]['reserva'] = True
                lista_livros[i]['status'] = True
                print(lista_livros[i])
                print(f"Informação atualizada! Livro {tituloLivro} disponível para reserva.")
            else:
                lista_livros[i]['reserva'] = False
                print(f"Informação atualizada! Livro {tituloLivro} indisponível para reserva.")
            break

'''def aluguel_unidades(titulolivro):
    global lista_livros
    alugado = 0
    for i in range (0, len(lista_livros)):
        if (lista_livros[i]['titulo']) == tituloLivro:
            qtd = lista_livros[i]['quantidade']
        else:
            print("Título não encontrado")
    for i in range(qtd):
        alugado += 1
    if qtd == alugado :
        lista_livros[i]['status']= False'''
            





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
        informacao_busca = input('Informe o TÍTULO do livro: ').upper()
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
                print (f"Status....: {lista_livros[i]['status']}")
                

    elif filtro == 2:
        informacao_busca = input('Informe o AUTOR do livro: ').upper()
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
                print (f"Status....: {lista_livros[i]['status']}")
                

    elif filtro == 3:
        informacao_busca = input('Informe o ANO do livro: ').upper()
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
                print (f"Status....: {lista_livros[i]['status']}")
                

    elif filtro == 4:
        informacao_busca = input('Informe o ASSUNTO do livro: ').upper()
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
                print (f"Status....: {lista_livros[i]['status']}")
                
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
        categorias.append(linha[0:-1])
    importa_tem = open("arqtematicas.txt", "r")
    while True:
        linha = importa_tem.readline()
        if(linha == ""):
            break
        tematicas.append(linha[0:-1])
    importa_liv = open("acervo.txt", "r")
    while True:
        linha = importa_liv.readline()[0:-1]
        if(linha == ""):
            break
        livro = {
            'titulo':linha,
            'autor': importa_liv.readline()[0:-1],
            'ano': int(importa_liv.readline()[0:-1]),
            'editora': importa_liv.readline()[0:-1],
            'edicao': importa_liv.readline()[0:-1],
            'quantidade':int(importa_liv.readline()[0:-1]),
            'assunto':importa_liv.readline()[0:-1] ,
            'reserva': bool(importa_liv.readline()[0:-1]),
            'categoria':importa_liv.readline()[0:-1],
            'tematica':importa_liv.readline()[0:-1],
            'status': bool(importa_liv.readline()[0:-1])

        }
        lista_livros.append(livro)
    importa_liv.close()
    importa_tem.close()
    importa_cat.close()
    #importa_fun = open("listafunc.txt","r")
    


def relatorios():

    global categorias
    global tematicas
    global lista_livros
    global data_atual


    tipo_relatorio = input("Digite C para relatórios sobre categorias,T para temáticas e A para acervo: ")

    if tipo_relatorio == "C" or "c":
        arquivo_categorias = open('relatorio_categorias.txt',"w")
        modelo_cat = open('relatorio_modelo_cat.txt', 'r')
        leitura_modelo_cat=modelo_cat.readlines()
        arquivo_categorias.writelines(leitura_modelo_cat)
        arquivo_categorias.write("          lista de categorias do acervo :\n")
        for i in range(0,len(categorias)):
            quantidade = i + 1
            arquivo_categorias.write("          "+ str(i + 1) + "."+ str(categorias[i] +'\n'))
        arquivo_categorias.write("           A quantidade de temáticas cadastradas é: " + str(quantidade)+"\n")
        arquivo_categorias.write("           Relatório gerado em : " + str(data_atual))
        arquivo_categorias.close()
        impressao_categorias = open('relatorio_modelo_cat.txt', "r")
        print(impressao_categorias.readlines())
        impressao_categorias.close()
    if tipo_relatorio == "T" or "t":
        arquivo_tematicas = open('relatorio_tematicas.txt',"w")
        modelo_tem = open('relatorio_modelo_tem.txt','r')
        leitura_modelo_tem = modelo_tem.readlines()
        arquivo_tematicas.writelines(leitura_modelo_tem)
        for i in range (0,len(tematicas)):
            quantidade = i + 1
            arquivo_tematicas.write("          "+ str(i + 1) + "."+ str(tematicas[i] +'\n'))
        arquivo_tematicas.write("A quantidade de temáticas cadastradas é: " + str(quantidade))
        arquivo_tematicas.write("           Relatório gerado em : " + str(data_atual))
        arquivo_tematicas.close()
        impressao_tematica = open('relatorio_tematicas.txt','r')
        print(impressao_tematica.readlines())
        impressao_tematica.close()
    if tipo_relatorio == "a" or "A":
        arquivo_acervo = open('relatorio_acervo.txt',"w")
        modelo = open('relatorio_modelo.txt','r')
        leitura_modelo = modelo.readlines()
        arquivo_acervo.writelines(leitura_modelo)
        soma = 0
        for livro in lista_livros:
            qtd_acervo = livro['quantidade']
            soma += qtd_acervo
        arquivo_acervo.write("           A quantidade do acervo atual é :")
        arquivo_acervo.write(str(soma)+"unidades"+'\n')
        lista_titulos = []
        for livro in lista_livros:
            titulo_livro = livro['titulo']
            lista_titulos.append(titulo_livro)
        lista_titulos.sort()
        arquivo_acervo.write("          lista de títulos do acervo :\n")
        for i in range(len(lista_titulos)):
            titulo = lista_titulos[i]
            arquivo_acervo.write("          "+str(titulo)+'\n')
        arquivo_acervo.write("           Relatório gerado em : " + str(data_atual))
        arquivo_acervo.close()
        impressao_acervo = open('relatorio_acervo.txt',"r")
        print(impressao_acervo.readlines())
        impressao_acervo.close()
    else:
        print("Relatório não identificado")



def status(titulo_status):
    global lista_livros
    global categorias
    global tematicas
    status_livro = False
    encontrado = False
    for i in range (0, len(lista_livros)) :
        if (lista_livros[i]['titulo']) == titulo_status :
            if lista_livros[i]['reserva'] == True:
                status_livro = True
                posicao = i
                encontrado = True
                break

    if encontrado == False :
        print("Título não encontrado!")
    else:
        if status_livro == True:
            if lista_livros[posicao]['status'] == True :
                print (f"\nTítulo....: {lista_livros[i]['titulo']}")
                print ("O Título buscado está no setor",f"Categoria.: {lista_livros[i]['categoria']}")
                print("Título buscado está na estante ",lista_livros[i]['tematica'])
                print( lista_livros[i]['quantidade'],"unidade(s) disponível(s)")

            else:
                print("Título encontra-se alugado. Data de devolução prevista...:")
        else: print("Título não está disponível para reserva")




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
                    status(input('Titulo do livro que deseja obter status ').upper())
                elif opcao == '11':
                    break
                else:
                    print("Opção inválida")



if __name__ == "__main__":
    main()