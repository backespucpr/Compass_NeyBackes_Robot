#- Baixe o arquivo do link JSON 1, abra ele no vsCode com Python nomeando-o
#como partida guarde em uma variável e printe o JSON inteiro no terminal.

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

#Python não consegue mostrar o arquivo json naturamenlte, por isso utilizamos json.load() que trasnforma os dados em
#um dicionário Python. Para identá-lo de uma forma melhor utilizei o pprint para que a saída fique um pouco mais organizada.
pprint.pprint(jsonRetornado)