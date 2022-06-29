#Do JSON 1 Guarde apenas o Nome do Estádio, o Placar e o Status do jogo dentro de variáveis e mostre-as.

#importando a biblioteca json
import json
#Importando a bilbioteca pprint para melhorar a impressão do dicionário
import pprint
#função como o metodo open para a leitura do arquivo json
def retornarJson():
    #precisei alterar como o caminho de acesso já que estou trabalhando com vscode na nuvem(gitpod) direto do próprio github.
    with open('/workspace/Compass_NeyBackes_Robot/python_exercicios_dados/arquivos_auxiliares/partida.json') as json_normal:
     jsonManipulavel = json.load(json_normal)
    return jsonManipulavel

#armazenando a leitura do arquivo em uma variável
jsonRetornado = retornarJson()

#Guardando os dados em variáves
placar = jsonRetornado['copa-do-brasil'][0]["placar"]
estadio = jsonRetornado['copa-do-brasil'][0]["estadio"]["nome_popular"]
statusJogo = jsonRetornado['copa-do-brasil'][0]["status"]
#Guardando as variáveis em um dicionário
resposta = {
    'Estadio': estadio,
    'Placar': placar,     
    'Status do Jogo': statusJogo
}
#impressão identada com pprint
pprint.pprint(resposta)