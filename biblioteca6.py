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


import os


def login (login,senha):
    for f in lista_funcionarios:
        if f[1] == login and f[2] == senha:
            return f[0]
    return None


def cadastro_categoria ():
    global categorias
    global tematicas

    cabecalho_sistema()

    print("     ┌────────────────────────────────────────────────────────────────────────────┐")
    print("     │                     =-=-= CADASTRAR CATEGORIA =-=-=                        │")
    print("     └────────────────────────────────────────────────────────────────────────────┘")
          
    arquivo_categorias = open("arqcategorias.txt","w")
    categoria = input("\n         » Digite o nome da categoria que deseja cadastrar: ").upper()
    if categoria in categorias :
        print("\n                    :: Categoria existente ::")
    else:
        categorias.append(categoria)
        print("\n                    :: Categoria adicionada com sucesso! ::")
        categorias.sort()
        for e in categorias:
            arquivo_categorias.write(e+"\n")
    arquivo_categorias.close()



def cadastro_tematica ():

    cabecalho_sistema()

    print("     ┌────────────────────────────────────────────────────────────────────────────┐")
    print("     │                     =-=-= CADASTRAR TEMÁTICA =-=-=                         │")
    print("     └────────────────────────────────────────────────────────────────────────────┘")

    arquivo_tematicas = open("arqtematicas.txt", "w")
    tematica = input("\n        » Digite o nome da temática que deseja cadastrar: ").upper()
    if tematica in tematicas :
        print("\n                    :: Temática existente ::")
    else:
        tematicas.append(tematica)
        print("\n                    :: Temática adicionada com sucesso! ::")
        tematicas.sort()
        for e in tematicas:
            arquivo_tematicas.write(e+"\n")
    arquivo_tematicas.close()


def update_acervo_arquivo():
    global lista_livros
    arquivo_acervo= open("acervo.txt", 'w')
    for e in lista_livros:
        arquivo_acervo.write(e['titulo']+"\n")
        arquivo_acervo.write(e['autor'] + "\n")
        arquivo_acervo.write(str(e['ano']) + "\n")
        arquivo_acervo.write(e['editora'] + "\n")
        arquivo_acervo.write(e['edicao'] + "\n")
        arquivo_acervo.write(str(e ['quantidade'])+"\n")
        arquivo_acervo.write(str(e ['qtdisponivel'])+"\n")
        arquivo_acervo.write(e['assunto']+"\n")
        arquivo_acervo.write(str(e['reserva']) + "\n")
        arquivo_acervo.write(str(e['categoria']) + "\n")
        arquivo_acervo.write(str(e['tematica'])+"\n")
        arquivo_acervo.write(str(e['status']) + "\n")
    arquivo_acervo.close()


def cadastro_livro():
    global tematicas
    global categorias
    global lista_livros

    cabecalho_sistema()

    print("     ┌────────────────────────────────────────────────────────────────────────────┐")
    print("     │                       =-=-= CADASTRAR LIVRO =-=-=                          │")
    print("     └────────────────────────────────────────────────────────────────────────────┘\n")
    


    livro = {
        'titulo':input("                      » Título....: ").upper(),
        'autor':input("                      » Autor.....: ").upper(),
        'ano':int(input("                      » Ano.......: ")),
        'editora':input("                      » Editora...: ").upper(),
        'edicao':input("                      » Edição....: "),
        'quantidade':int(input("                      » Quantidade: ")),
        'qtdisponivel': int(input("                      » Qtde Disponível: ")),
        'assunto':input("                      » Assunto...: ").upper(),
        'reserva': False,
        'status': False
    }
    print("     ├────────────────────────────── CATEGORIAS ──────────────────────────────────┤\n")
    
    for i in range (0, len(categorias)):
        print (f'                      [{i+1}] - {categorias[i]}')
    posicao = int(input('\n                      » Informe o codigo da categoria do livro: '))-1
    livro ['categoria'] = categorias[posicao]


    print("     ├────────────────────────────── TEMÁTICAS ───────────────────────────────────┤\n")
    for i in range (0, len(tematicas)):
        print (f'                      [{i+1}] - {tematicas[i]}')
    posicao = int(input('                      » Informe o codigo da temática do livro: '))-1
    livro ['tematica'] = tematicas[posicao]
    lista_livros.append(livro)


    print("\n                      :: Livro cadastrado com sucesso! ::")
    update_acervo_arquivo()


def habilita_reserva():
    global lista_livros
    os.system("cls")
    cabecalho_sistema()
    localiza = False

    print("     ┌────────────────────────────────────────────────────────────────────────────┐")
    print("     │                   =-=-= HABILITAR RESERVA DE LIVRO =-=-=                   │")
    print("     └────────────────────────────────────────────────────────────────────────────┘\n")
    

    tituloLivro = input('\n                 » Titulo do livro para alterar disponibilidade: ').upper()
    
    reservar = input('\n                 » Disponibilizar livro para reserva [S/N]? ')

    for i in range (0, len(lista_livros)):
        if (lista_livros[i]['titulo']) == tituloLivro:
            localiza = True
            if reservar in 'Ss':
                lista_livros[i]['reserva'] = True
                lista_livros[i]['status'] = True
                print(f"\n       :: Informação atualizada! Livro {tituloLivro} disponível para reserva. ::")
            else:
                lista_livros[i]['reserva'] = False
                print(f"\n       :: Informação atualizada! Livro {tituloLivro} indisponível para reserva. ::")
            break

    if localiza == False:
        print('\n                      :: Livro não localizado! ::')

    update_acervo_arquivo()

            

def ajusta_acervo():
    global lista_livros
    cabecalho_sistema()
    localiza = False

    print("     ┌────────────────────────────────────────────────────────────────────────────┐")
    print("     │                   =-=-= AJUSTAR ESTOQUE DO ACERVO =-=-=                    │")
    print("     └────────────────────────────────────────────────────────────────────────────┘\n")

    tituloLivro = input('          »» Titulo do livro para ajustar estoque: ').upper()

    for i in range(0, len(lista_livros)):
        if (lista_livros[i]['titulo']) == tituloLivro:
            localiza = True
            qtd_alugada = lista_livros[i]["quantidade"] - lista_livros[i]["qtdisponivel"]
            qtd_atual = lista_livros[i]["quantidade"]

            print(f'\n                   Livro...........: {lista_livros[i]["titulo"]}')
            print(f'                   Estoque atual...: {lista_livros[i]["quantidade"]} un')
            print(f'                   Qtde alugada....: {qtd_alugada} un')
            print(f'                   Qtde disponível.: {lista_livros[i]["qtdisponivel"]} un')

            qtd_nova = int(input('\n          »» Digite a nova quantidade em estoque: '))
            lista_livros[i]['quantidade'] = qtd_nova
            lista_livros[i]["qtdisponivel"] = lista_livros[i]["qtdisponivel"] + (qtd_nova - qtd_atual)

            print(f'\n                   Livro...........: {lista_livros[i]["titulo"]}')
            print(f'                   Estoque atual...: {lista_livros[i]["quantidade"]} un')
            print(f'                   Qtde alugada....: {qtd_alugada} un')
            print(f'                   Qtde disponível.: {lista_livros[i]["qtdisponivel"]} un')
            break

    update_acervo_arquivo()

    if localiza == False:
        print('\n                      :: Livro não localizado! ::')


def remove_livro():
    global lista_livros
    localiza = False
    cabecalho_sistema()

    print("     ┌────────────────────────────────────────────────────────────────────────────┐")
    print("     │                    =-=-= REMOVER LIVRO DO ACERVO =-=-=                     │")
    print("     └────────────────────────────────────────────────────────────────────────────┘\n")

    tituloLivro = input('               »» Titulo do livro deseja remover: ').upper()

    for i in range (0, len(lista_livros)):
        if (lista_livros[i]['titulo']) == tituloLivro:
            localiza = True

            lista_livros.pop(i)
            print(f"\n                 :: Livro {tituloLivro} removido com sucesso! ::")

    if localiza == False:
        print('\n                      :: Livro não localizado! ::')

    update_acervo_arquivo()


def busca_livro():

    global lista_livros
    cabecalho_sistema()
    localiza = False

    print("     ┌────────────────────────────────────────────────────────────────────────────┐")
    print("     │                        =-=-= BUSCAR LIVRO =-=-=                            │")
    print("     └────────────────────────────────────────────────────────────────────────────┘")
    print("\n                   [1] Título - [2] Autor - [3] Ano - [4] Assunto")

    filtro = int(input("\n             » Informe o filtro a ser utilizado na busca: "))

    if filtro == 1:
        informacao_busca = input('\n                    » Informe o TÍTULO do livro: ').upper()
        for i in range (0, len(lista_livros)):
            if (lista_livros[i]['titulo']) == informacao_busca:
                localiza = True
                print (f"\n                    »    Título....: {lista_livros[i]['titulo']}")
                print (f"                    »    Autor.....: {lista_livros[i]['autor']}")
                print (f"                    »    Ano.......: {lista_livros[i]['ano']}")
                print (f"                    »    Editora...: {lista_livros[i]['editora']}")
                print (f"                    »    Assunto...: {lista_livros[i]['assunto']}")
                print (f"                    »    Categoria.: {lista_livros[i]['categoria']}")
                print (f"                    »    Temática..: {lista_livros[i]['tematica']}")
                print (f"                    »    Reserva...: {lista_livros[i]['reserva']}")
                print (f"                    »    Status....: {lista_livros[i]['status']}")


    elif filtro == 2:
        informacao_busca = input('\n                    » Informe o AUTOR do livro: ').upper()
        for i in range (0, len(lista_livros)):
            if (lista_livros[i]['autor']) == informacao_busca:
                localiza = True
                print (f"\n                    »    Título....: {lista_livros[i]['titulo']}")
                print (f"                    »    Autor.....: {lista_livros[i]['autor']}")
                print (f"                    »    Ano.......: {lista_livros[i]['ano']}")
                print (f"                    »    Editora...: {lista_livros[i]['editora']}")
                print (f"                    »    Assunto...: {lista_livros[i]['assunto']}")
                print (f"                    »    Categoria.: {lista_livros[i]['categoria']}")
                print (f"                    »    Temática..: {lista_livros[i]['tematica']}")
                print (f"                    »    Reserva...: {lista_livros[i]['reserva']}")
                print (f"                    »    Status....: {lista_livros[i]['status']}")


    elif filtro == 3:
        informacao_busca = input('\n                    » Informe o ANO do livro: ').upper()
        for i in range (0, len(lista_livros)):
            if (lista_livros[i]['ano']) == informacao_busca:
                localiza = True
                print (f"\n                    »    Título....: {lista_livros[i]['titulo']}")
                print (f"                    »    Autor.....: {lista_livros[i]['autor']}")
                print (f"                    »    Ano.......: {lista_livros[i]['ano']}")
                print (f"                    »    Editora...: {lista_livros[i]['editora']}")
                print (f"                    »    Assunto...: {lista_livros[i]['assunto']}")
                print (f"                    »    Categoria.: {lista_livros[i]['categoria']}")
                print (f"                    »    Temática..: {lista_livros[i]['tematica']}")
                print (f"                    »    Reserva...: {lista_livros[i]['reserva']}")
                print (f"                    »    Status....: {lista_livros[i]['status']}")


    elif filtro == 4:
        informacao_busca = input('\n                    » Informe o ASSUNTO do livro: ').upper()
        for i in range (0, len(lista_livros)):
            if (lista_livros[i]['assunto']) == informacao_busca:
                localiza = True
                print (f"\n                    »    Título....: {lista_livros[i]['titulo']}")
                print (f"                    »    Autor.....: {lista_livros[i]['autor']}")
                print (f"                    »    Ano.......: {lista_livros[i]['ano']}")
                print (f"                    »    Editora...: {lista_livros[i]['editora']}")
                print (f"                    »    Assunto...: {lista_livros[i]['assunto']}")
                print (f"                    »    Categoria.: {lista_livros[i]['categoria']}")
                print (f"                    »    Temática..: {lista_livros[i]['tematica']}")
                print (f"                    »    Reserva...: {lista_livros[i]['reserva']}")
                print (f"                    »    Status....: {lista_livros[i]['status']}")

    else:
        print('          ::  Opção Inválida!  ::')

    if localiza == False:
        print('\n                      :: Livro não localizado! ::')



def aluguel_livros():

    global lista_livros
    cabecalho_sistema()

    print("     ┌────────────────────────────────────────────────────────────────────────────┐")
    print("     │                      =-=-= LOCAÇÃO DE  LIVROS =-=-=                        │")
    print("     └────────────────────────────────────────────────────────────────────────────┘")
    print("\n                   [1] Aluguel de Livro - [2] Devolução de Livro")

    filtro = int(input("\n                    » Informe o módulo a ser acionado: "))

    if filtro == 1:
        informacao_busca = input('\n                    » Informe o TÍTULO do livro:').upper()
        for i in range(0, len(lista_livros)):
            if (lista_livros[i]['titulo']) == informacao_busca:
                if (lista_livros[i]['reserva']) == True:
                    if lista_livros[i]['qtdisponivel'] > 0:
                        lista_livros[i]['qtdisponivel'] = lista_livros[i]['qtdisponivel'] - 1
                        print("\n          :: Locação concluída! ::")
                        break
                    else:
                        print("          :: Todas as unidades estão alugadas! ::")
                else:
                    print("          :: O Livro não está disponível para locação! ::")
            else:
                print("          :: Livro não localizado! ::")

    elif filtro == 2:
        informacao_busca = input('\n                    » Informe o TÍTULO do livro:').upper()
        for i in range(0, len(lista_livros)):
            if (lista_livros[i]['titulo']) == informacao_busca:
                lista_livros[i]['qtdisponivel'] = lista_livros[i]['qtdisponivel'] + 1
                print("          :: Devolução concluída! ::")
            else:
                print("          :: Livro não localizado! ::")
    else:
        print("          :: Opção Inválida! ::")

    update_acervo_arquivo()




'''


def aluguel_livros():

    global lista_livros
    cabecalho_sistema()

    print("     ┌────────────────────────────────────────────────────────────────────────────┐")
    print("     │                      =-=-= LOCAÇÃO DE  LIVROS =-=-=                        │")
    print("     └────────────────────────────────────────────────────────────────────────────┘")
    print("\n                   [1] Aluguel de Livro - [2] Devolução de Livro")

    filtro = int(input("\n                    » Informe o módulo a ser acionado: "))

    if filtro == 1:
        informacao_busca = input('\n                    » Informe o TÍTULO do livro: ').upper()
        for i in range(0, len(lista_livros)):
            if lista_livros[i]['titulo'] == informacao_busca:
                if lista_livros[i]['reserva'] == True:
                    if lista_livros[i]['qtdisponivel'] > 0:
                        lista_livros[i]['qtdisponivel'] = lista_livros[i]['qtdisponivel'] - 1
                        print(f'                   Estoque atual...: {lista_livros[i]["quantidade"]} un')
                        print(f'                   Qtde disponível.: {lista_livros[i]["qtdisponivel"]} un')
                        print("\n                    :: Locação concluída! ::")
                        break

                    else:
                        print("\n          :: Todas as unidades estão alugadas! ::")
                else:
                    print("\n          :: O Livro não está disponível para locação! ::")
            else:
                print("\n                    :: Livro não localizado! ::")

    elif filtro == 2:
        informacao_busca = input('\n                    » Informe o TÍTULO do livro: ').upper()

        for i in range(0, len(lista_livros)):
            if lista_livros[i]['titulo'] == informacao_busca:
                lista_livros[i]['qtdisponivel'] = lista_livros[i]['qtdisponivel'] + 1
                print(f'                   Estoque atual...: {lista_livros[i]["quantidade"]} un')
                print(f'                   Qtde disponível.: {lista_livros[i]["qtdisponivel"]} un')
                print("                    :: Devolução concluída! ::")
                break
            else:
                print("                    :: Livro não localizado! ::")
    else:
        print("                            :: Opção Inválida! ::")

    update_acervo_arquivo()
'''

def repete_funcao(funcao):
    continua = 'N'
    while continua in 'Nn':
        funcao()
        print("\n     └────────────────────────────────────────────────────────────────────────────┘")
        continua = input("\n                          » Voltar ao menu principal [S/N]? ")

    cabecalho_sistema()


def importa_dados():

    global lista_livros
    cabecalho_sistema()

    print("     ┌────────────────────────────────────────────────────────────────────────────┐")
    print("     │                 =-=-= IMPORTAR ARQUIVO DE LIVROS =-=-=                     │")
    print("     └────────────────────────────────────────────────────────────────────────────┘\n")

    import_arquivo = input("          »» Digite o arquivo que deseja importar: ")
    importa_liv = open(import_arquivo, "r")

    while True:
        linha = importa_liv.readline()[0:-1]
        if (linha == ""):
            break
        livro = {
            'titulo': linha,
            'autor': importa_liv.readline()[0:-1],
            'ano': int(importa_liv.readline()[0:-1]),
            'editora': importa_liv.readline()[0:-1],
            'edicao': importa_liv.readline()[0:-1],
            'quantidade': int(importa_liv.readline()[0:-1]),
            'qtdisponivel': int(importa_liv.readline()[0:-1]),
            'assunto': importa_liv.readline()[0:-1],
            'reserva': bool(importa_liv.readline()[0:-1]),
            'categoria': importa_liv.readline()[0:-1],
            'tematica': importa_liv.readline()[0:-1],
            'status': bool(importa_liv.readline()[0:-1])

        }
        lista_livros.append(livro)
        print("          :: Dados importados com sucesso! ::")
    importa_liv.close()

    update_acervo_arquivo()



def import_inicial():
    global categorias
    global tematicas
    global lista_livros
    
    importa_cat = open("arqcategorias.txt", "r")
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
            'qtdisponivel':int(importa_liv.readline()[0:-1]),
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



def cabecalho_sistema():
    os.system("cls")
    print("\n     ╔════════════════════════════════════════════════════════════════════════════╗")
    print("     ║             MORAIS LIBRARY - Sistema de Gestão Bibliotecária               ║")
    print("     ╚════════════════════════════════════════════════════════════════════════════╝\n")



def relatorios():

    global categorias
    global tematicas
    global lista_livros
    cabecalho_sistema()

    print("     ┌────────────────────────────────────────────────────────────────────────────┐")
    print("     │                         =-=-= RELATÓRIOS =-=-=                             │")
    print("     └────────────────────────────────────────────────────────────────────────────┘")
    print("\n                 [1] Acervo de Livros - [2] Categorias - [3] Temáticas")
          
  
    tipo_relatorio = int(input('\n                 » Informe o relatório desejado: '))

    
    if tipo_relatorio == 1:
        
        arquivo_acervo = open("relatorio_acervo.txt","w")
        modelo = open("relatorio_modelo.txt", "r")# encoding="utf-8")
        leitura_modelo=modelo.readlines()
        arquivo_acervo.writelines(leitura_modelo)

        somaestoque = 0
        somatitulos = 0
        somadisponivel = 0
        
        arquivo_acervo.write("                           »» RELATÓRIO DE TÍTULOS DO ACERVO ««\n")
        
        for i in range(len(lista_livros)):
            somatitulos += 1
            somaestoque += lista_livros[i]['quantidade']
            somadisponivel += lista_livros[i]['qtdisponivel']
            arquivo_acervo.write("\n                         Título : "+str(lista_livros[i]['titulo'])+"\n")
            arquivo_acervo.write("                        | Estoque Total: "+str(lista_livros[i]['quantidade']))
            arquivo_acervo.write(" | Volumes alugados: "+str((lista_livros[i]['quantidade']-lista_livros[i]['qtdisponivel']))+" |\n")



        arquivo_acervo.write("\n                        -------- RESUMO SINTÉTICO DE ESTOQUE --------")
        arquivo_acervo.write("\n                             Total de Títulos.............:")
        arquivo_acervo.write(str(somatitulos))
        arquivo_acervo.write("\n                             Total de Volumes em Estoque..: ")
        arquivo_acervo.write(str(somaestoque))
        arquivo_acervo.write("\n                             Total de Volumes Alugados....: ")
        arquivo_acervo.write(str(somadisponivel))
        arquivo_acervo.write("     ------------------------------------------------------------------------------\n")
        arquivo_acervo.write("      Relatório gerado em : " + str(data_atual) + "            Arquivo: relatorio_acervo.txt")
        arquivo_acervo.close()
        
        print("\n                :: Relatório gerado com sucesso! ::")
        print("\n                 » » »  [relatorio_acervo.txt] « « «")
        

    
    elif tipo_relatorio == 2:
        arquivo_categorias = open("relatorio_categorias.txt","w")
        modelo = open("relatorio_modelo.txt", "r", )#encoding="utf-8")
        leitura_modelo=modelo.readlines()
        arquivo_categorias.writelines(leitura_modelo)
        arquivo_categorias.write("\n                           »» RELATÓRIO DE CATEGORIAS DO ACERVO ««\n")
        for i in range(0,len(categorias)):
            arquivo_categorias.write("                           - "+str(categorias[i])+"\n")

        arquivo_categorias.write("\n                    Total de Categorias Cadastradas....: ")
        arquivo_categorias.write(str(len(categorias))+"\n")
        arquivo_categorias.write("     ------------------------------------------------------------------------------\n")
        arquivo_categorias.write("     Relatório gerado em : " + str(data_atual) + "            Arquivo: relatorio_categorias.txt")
        arquivo_categorias.close()
        print("\n                :: Relatório gerado com sucesso! ::")
        print("\n               » » »  [relatorio_categoria.txt] « « «")

    
    elif tipo_relatorio == 3:
        arquivo_tematicas = open('relatorio_tematicas.txt',"w")
        modelo = open('relatorio_modelo.txt', 'r')
        leitura_modelo = modelo.readlines()
        arquivo_tematicas.writelines(leitura_modelo)
        arquivo_tematicas.write("\n                           »» RELATÓRIO DE TEMÁTICAS DO ACERVO ««\n")
        for i in range(0, len(tematicas)):
            arquivo_tematicas.write("                           - "+str(tematicas[i]) + "\n")

        arquivo_tematicas.write("\n                    Total de Tematicas Cadastradas....: ")
        arquivo_tematicas.write(str(len(tematicas)) + "\n")
        arquivo_tematicas.write("     ------------------------------------------------------------------------------\n")
        arquivo_tematicas.write("      Relatório gerado em : " + str(data_atual) + "            Arquivo: relatorio_tematicas.txt")
        arquivo_tematicas.close()
        print("\n                :: Relatório gerado com sucesso! ::")
        print("\n               » » »  [relatorio_tematicas.txt] « « «")
    
    else: 
        print("\n                ::     Relatório inexistente!   ::")



def status():

    global lista_livros
    global categorias
    global tematicas
    status_livro = False
    encontrado = False
    cabecalho_sistema()
    print("     ┌────────────────────────────────────────────────────────────────────────────┐")
    print("     │                      =-=-= STATUS DO LIVRO =-=-=                           │")
    print("     └────────────────────────────────────────────────────────────────────────────┘")

    titulo_status = input('\n          »» Titulo do livro que deseja obter status: ').upper()

    for i in range (0, len(lista_livros)) :
        if (lista_livros[i]['titulo']) == titulo_status :
            encontrado = True
            if lista_livros[i]['reserva'] == True:
                status_livro = True
                posicao = i
                break

    if encontrado == False :
        print("         :: Título não encontrado! ::")
    else:
        if status_livro == True:
            if lista_livros[posicao]['status'] == True :
                print(f"\n                    »    Título.....: {lista_livros[i]['titulo']}")
                print(f"                    »    Setor......: {lista_livros[i]['categoria']}")
                print(f"                    »    Estante....: {lista_livros[i]['tematica']}")
                print(f"                    »    Estoque....: {lista_livros[i]['quantidade']}")
                print(f"                    »    Alugados...: {(lista_livros[i]['quantidade']-lista_livros[i]['qtdisponivel'])}")
                print(f"                    »    Disponíveis: {lista_livros[i]['qtdisponivel']}")

        else: print("          :: Título não está disponível para reserva! :: ")




def menu():
    cabecalho_sistema()
    print("     ┌────────────────────────────────────────────────────────────────────────────┐")
    print("     │             =-=-=-=-=-=-=-= MENU PRINCIPAL =-=-=-=-=-=-=-=                 │")
    print("     ├────────────────────────────────────────────────────────────────────────────┤")
    print("     │                   1  - CADASTRAR CATEGORIA                                 │")
    print("     │                   2  - CADASTRAR TEMÁTICA                                  │")
    print("     │                   3  - CADASTRAR LIVRO                                     │")
    print("     │                   4  - HABILITAR RESERVA                                   │")
    print("     │                   5  - ATUALIZAR QUANTIDADE DE EXEMPLARES                  │")
    print("     │                   6  - REMOVER TÍTULO                                      │")
    print("     │                   7  - BUSCAR LIVRO                                        │")
    print("     │                   8  - IMPORTAR DADOS                                      │")
    print("     │                   9  - RELATÓRIOS                                          │")
    print("     │                   10 - STATUS DO LIVRO                                     │")
    print("     │                   11 - LOCAÇÃO DE LIVROS                                   │")
    print("     │                   12 - Sair                                                │")
    print("     └────────────────────────────────────────────────────────────────────────────┘")

    return input("\n                        Digite a opção desejada: ")
    


def main():
    cabecalho_sistema()
    tentativas = 0
    import_inicial()

    while True:
        login_func = input("                » Digite seu login: ")
        senha_func = input("                » Digite sua senha: ")
        nome = login (login_func,senha_func)
        if nome == None:
            print("\n                :: Login ou senha inválido, digite novamente! ::\n")
            tentativas+=1
            if tentativas >= 3 :
                print("\n         :: Esqueceu sua senha? Entre em contato com o administrador! ::\n")
                return
        else:
            tentativas=0

            cabecalho_sistema()

            print("                           Bem vindo,",nome)

            while True:
                opcao = menu()
                if opcao == '1':
                    repete_funcao(lambda: cadastro_categoria())
                elif opcao == '2':
                    repete_funcao(lambda: cadastro_tematica())
                elif opcao == '3':
                    repete_funcao(lambda: cadastro_livro())
                elif opcao == '4':
                    repete_funcao(lambda: habilita_reserva())
                elif opcao == '5':
                    repete_funcao(lambda: ajusta_acervo())
                elif opcao == '6':
                    repete_funcao(lambda: remove_livro())
                elif opcao == '7':
                    repete_funcao(lambda: busca_livro())
                elif opcao == '8':
                    repete_funcao(lambda: importa_dados())
                elif opcao == '9':
                    repete_funcao(lambda: relatorios())
                elif opcao == '10':
                    repete_funcao(lambda: status())
                elif opcao == '11':
                    repete_funcao(lambda: aluguel_livros())
                elif opcao == '12':
                    break
                else:
                    print("Opção inválida")



if __name__ == "__main__":
    main()