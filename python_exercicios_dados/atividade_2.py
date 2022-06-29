#Pegue o arquivo JSON 1 e printe apenas o nome do time vencedor no terminal.

#importando a biblioteca json
import json
#função como o metodo open para a leitura do arquivo json
def retornarJson():
    #precisei alterar como o caminho de acesso já que estou trabalhando com vscode na nuvem(gitpod) direto do próprio github.
    with open('/workspace/Compass_NeyBackes_Robot/python_exercicios_dados/arquivos_auxiliares/partida.json') as json_normal:
     jsonManipulavel = json.load(json_normal)
    return jsonManipulavel

#armazenando a leitura do arquivo em uma variável
jsonRetornado = retornarJson()
#Dicionarios dentro de dicionários, assim acessei o dicionario copa-do-brasil para acessar time_mandante
#e o conteúdo que estava localizado na chave nome_popular
timeVencedor = jsonRetornado['copa-do-brasil'][0]['time_mandante']['nome_popular']
print(timeVencedor)


