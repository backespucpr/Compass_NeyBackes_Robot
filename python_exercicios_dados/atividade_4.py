 #No JSON 1 printe todas as chaves e valores do time visitante

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
#guardando dados do time visitante
timeVisitante = jsonRetornado['copa-do-brasil'][0]["time_visitante"]

#impressão identada com pprint
pprint.pprint(timeVisitante)

