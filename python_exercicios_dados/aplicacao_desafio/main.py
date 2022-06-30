import pandas as pd

df = pd.read_csv('/workspace/Compass_NeyBackes_Robot/python_exercicios_dados/aplicacao_desafio/tabela.csv')
#Retorn todos os simbolos da tabela
def tabelaSimbolos():
    return df['Simbolo']
#Retorna todos os nomes da tabela
def tabelaNomes():
    return df['Nome']
#Busca os elemento pelo simbolo
def buscarElememento(busca):
    index = df.index    
    condicao = df["Simbolo"] == busca    
    indiceSimbolo = index[condicao]
    indiceElemento = indiceSimbolo.tolist()
    s = [str(integer) for integer in indiceElemento]
    a_string = "".join(s)
    res = int(a_string)
    return df.loc[res]

def menuTabela():
    def print_menu():       
        print(30 * "-", "Aplicação CSV menu", 30 * "-")
        print("1. Listar todos os simbolos dos elementos na tabela ")
        print("2. Listar todos os nomes dos elementos na tabela")
        print("3. Listar todos os dados de um determinado elemento")
        print("4. Listar todos os dados da tabela ")        
        print("5. Encerrar aplicação ")
        print(73 * "-")

    menu = True

    intEscolha = -1

    while menu:    
        print_menu()    # Mostrar menu
        escolha = input("Escolha uma opção 1 - 5: ")

        if escolha == '1':
            intEscolha = 1
            print(tabelaSimbolos())
            menu = False
        elif escolha == '2':            
            intEscolha = 2
            print(tabelaNomes())
            menu = False
        elif escolha == '3':                    
            intEscolha = 3
            busca = str(input('Informe o simbolo do elemento que você quer encontrar nesta tabela: '))
            print(buscarElememento(busca))
            menu = False
        elif escolha == '4':            
            intEscolha = 4
            menu = False
        elif escolha == '5':
            intEscolha = -1
            print("Exiting..")
            menu = False  # encerra o menu
        else:
            # se colocar algum valor diferente ele vai aparecer uma mensagem de erro
            input("Opção errada! Por favor, escolha as opções do menu")
    


print(menuTabela())



