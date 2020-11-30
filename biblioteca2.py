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

import os
import os
print(os.getcwd())

def login (login,senha):
    for f in lista_funcionarios:
        if f[1] == login and f[2] == senha:
            return f[0]
    return None


def cadastro_categoria ():
    global categorias
    global tematicas
    os.system("cls")
    cabecalho_sistema()

    print("     ┌────────────────────────────────────────────────────────────────────────────┐")
    print("     │                     =-=-= CADASTRAR CATEGORIA =-=-=                        │")
    print("     └────────────────────────────────────────────────────────────────────────────┘")
          
    arquivo_categorias = open("TESTE.txt.txt","w")
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
    os.system("cls")
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


def cadastro_livro():
    global tematicas
    global categorias
    global lista_livros
    os.system("cls")
    cabecalho_sistema()

    print("     ┌────────────────────────────────────────────────────────────────────────────┐")
    print("     │                       =-=-= CADASTRAR LIVRO =-=-=                          │")
    print("     └────────────────────────────────────────────────────────────────────────────┘\n")
    
    arquivo_acervo= open("acervo.txt", "w")

    livro = {
        'titulo':input("                      » Título....: ").upper(),
        'autor':input("                      » Autor.....: ").upper(),
        'ano':int(input("                      » Ano.......: ")),
        'editora':input("                      » Editora...: ").upper(),
        'edicao':input("                      » Edição....: "),
        'quantidade':int(input("                      » Quantidade: ")),
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

    print("\n                      :: Livro cadastrado com sucesso! ::")
    arquivo_acervo.close()


def habilita_reserva():
    global lista_livros
    os.system("cls")
    cabecalho_sistema()

    print("     ┌────────────────────────────────────────────────────────────────────────────┐")
    print("     │                   =-=-= HABILITAR RESERVA DE LIVRO =-=-=                   │")
    print("     └────────────────────────────────────────────────────────────────────────────┘\n")
    

    tituloLivro = input('\n                      » Titulo do livro para alterar disponibilidade: ').upper()
    
    reservar = input('\n                      » Disponibilizar livro para reserva [S/N]? ')

    for i in range (0, len(lista_livros)):
        if (lista_livros[i]['titulo']) == tituloLivro:
            if reservar in 'Ss':
                lista_livros[i]['reserva'] = True
                print(lista_livros[i])
                print(f"\n               :: Informação atualizada! Livro {tituloLivro} disponível para reserva. ::")
            else:
                lista_livros[i]['reserva'] = False
                print(f"\n               :: Informação atualizada! Livro {tituloLivro} indisponível para reserva. ::")
            break
    print('\n                      :: Livro não localizado! ::')

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
    os.system("cls")
    cabecalho_sistema()

    print("     ┌────────────────────────────────────────────────────────────────────────────┐")
    print("     │                   =-=-= AJUSTAR ESTOQUE DO ACERVO =-=-=                    │")
    print("     └────────────────────────────────────────────────────────────────────────────┘\n")
 
    for i in range (0, len(lista_livros)):
        if (lista_livros[i]['titulo']) == tituloLivro:
            print(f'                      Livro: {lista_livros[i]["titulo"]}')
            print(f'                      Estoque: {lista_livros[i]["quantidade"]} un')
            lista_livros[i]['quantidade'] = int(input('\n                      » Digite a nova quantidade em estoque: '))
            print('\n                      :: Quantidade de exemplares ajustada com sucesso! ::') 
            print(f'\n                      :: A nova quantidade de acervo do livro {lista_livros[i]["titulo"]} é {lista_livros[i]["quantidade"]} un ::') 
            break
    
    print('\n                      :: Livro não localizado! ::') 

    


def remove_livro(tituloLivro):
    global lista_livros
    os.system("cls")
    cabecalho_sistema()

    print("     ┌────────────────────────────────────────────────────────────────────────────┐")
    print("     │                    =-=-= REMOVER LIVRO DO ACERVO =-=-=                     │")
    print("     └────────────────────────────────────────────────────────────────────────────┘\n")
 
    for i in range (0, len(lista_livros)):
        if (lista_livros[i]['titulo']) == tituloLivro:
            print (lista_livros[i])
            lista_livros.pop(i)
            break

    print(f"\n                      :: Livro {tituloLivro} removido com sucesso! ::")


def busca_livro():

    global lista_livros
    os.system("cls")
    cabecalho_sistema()

    print("     ┌────────────────────────────────────────────────────────────────────────────┐")
    print("     │                        =-=-= BUSCAR LIVRO =-=-=                            │")
    print("     └────────────────────────────────────────────────────────────────────────────┘")
    print("\n                   [1] Título - [2] Autor - [3] Ano - [4] Assunto")
          
    filtro = int(input("\n                    » Informe o filtro a ser utilizado na busca: "))
    
    if filtro == 1:
        informacao_busca = input('\n                    » Informe o TÍTULO do livro:').upper()
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
        informacao_busca = input('\n                    » Informe o AUTOR do livro: ').upper()
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
        informacao_busca = input('\n                    » Informe o ANO do livro: ').upper()
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
        informacao_busca = input('\n                    » Informe o ASSUNTO do livro: ').upper()
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
        continua = input('\n                    » Fazer novo cadastro [S/N]? ')
    os.system("cls")
    cabecalho_sistema()


def importa_dados(import_arquivo):
    importar = open(import_arquivo,"r")
    print(importar.readlines())

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
    print("\n     ╔════════════════════════════════════════════════════════════════════════════╗")
    print("     ║             MORAIS LIBRARY - Sistema de Gestão Bibliotecária               ║")
    print("     ╚════════════════════════════════════════════════════════════════════════════╝\n")


def relatorios():

    global categorias
    global tematicas
    global lista_livros
    os.system("cls")
    cabecalho_sistema()

    print("     ┌────────────────────────────────────────────────────────────────────────────┐")
    print("     │                         =-=-= RELATÓRIOS =-=-=                             │")
    print("     └────────────────────────────────────────────────────────────────────────────┘")
    print("\n                 [1] Acervo de Livros - [2] Categorias - [3] Temáticas")
          
  
    tipo_relatorio = int(input('\n                 » Informe o relatório desejado: '))

    
    if tipo_relatorio == 1:
        
        arquivo_acervo = open("relatorio_acervo.txt","w")
        modelo = open("relatorio_modelo.txt", "r", encoding="utf-8")
        leitura_modelo=modelo.readlines()
        arquivo_acervo.writelines(leitura_modelo)
        
        somaestoque = 0
        somatitulos = 0
        
        lista_titulos = []
        
        for livro in lista_livros:
            titulo_livro = livro['titulo']
            lista_titulos.append(titulo_livro)
        lista_titulos.sort()
        arquivo_acervo.write("                           »» RELATÓRIO DE TÍTULOS DO ACERVO ««\n")
        
        for i in range(len(lista_titulos)):
            titulo = lista_titulos[i]
            somatitulos += 1
            arquivo_acervo.write("                      - "+str(titulo)+'\n')
        arquivo_acervo.write("                      Total de títulos :")
        arquivo_acervo.write(str(somatitulos)+'\n')
            
        for livro in lista_livros:
            qtd_acervo = livro['quantidade']
            somaestoque += qtd_acervo
        arquivo_acervo.write("                          Total de volumes em estoque:")
        arquivo_acervo.write(str(somaestoque)+'\n')
        
        arquivo_acervo.close()
        
        print("\n                :: Relatório gerado com sucesso! ::")
        
        #impressao_acervo = open('relatorio_acervo.txt',"r")
        #print(impressao_acervo.readlines())
        #impressao_acervo.close()
    
    elif tipo_relatorio == 2:
        
        arquivo_categorias = open("relatorio_categorias2.txt","w")
        modelo = open("relatorio_modelo.txt", "r", encoding="utf-8")
        leitura_modelo=modelo.readlines()
        arquivo_categorias.writelines(leitura_modelo)
        arquivo_categorias.write("                           »» RELATÓRIO DE CATEGORIAS DO ACERVO ««\n")
        for i in categorias:
            arquivo_categorias.write(categorias[i]+"\n")
        arquivo_categorias.close()
        import shutil
        shutil.copy("relatorio_categorias2.txt", "prn")
        #impressao_categorias = open('relatorio_modelo.txt', "r")
        #print(impressao_categorias.readlines())
        #impressao_categorias.close()
    
    elif tipo_relatorio == 3:
        arquivo_tematicas = open('relatorio_tematicas.txt',"w")
        modelo = open('relatorio_modelo.txt', 'r')
        leitura_modelo = modelo.readlines()
        arquivo_tematicas.writelines(leitura_modelo)
        arquivo_tematicas.write("                           »» RELATÓRIO DE TEMÁTICAS DO ACERVO ««\n")
        for i in range(0, len(tematicas)):
            arquivo_tematicas.write(str(tematicas[i]) + "\n")
        arquivo_tematicas.write("           Relatório gerado em : " + str(data_atual))
        arquivo_tematicas.close()
        print("\n                :: Relatório gerado com sucesso! ::")
    
    else: 
        print("\n                :: Relatório inexistente ::")


def status(titulo_status):
    global lista_livros
    global categorias
    global tematicas
    status_livro = False
    encontrado = False
    for i in range (0, len(lista_livros)) :
        if (lista_livros[i]['titulo']) == titulo_status :
            encontrado = True
            if lista_livros[i]['reserva'] == True:
                status_livro = True
                posicao = i
                break
            encontrado=True
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
    print("     │                   11 - Sair                                                │")
    print("     └────────────────────────────────────────────────────────────────────────────┘")

    return input("\n                        Digite a opção desejada:")
    


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
            os.system("cls")
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
                    habilita_reserva()
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