 #Percorra o JSON 2, utilizando o loop FOR e printe suas chaves principais.

#importando a biblioteca json
import json
#Importando a bilbioteca pprint para melhorar a impressão do dicionário
import pprint
#função como o metodo open para a leitura do arquivo json
def retornarJson():
    #precisei alterar como o caminho de acesso já que estou trabalhando com vscode na nuvem(gitpod) direto do próprio github.
    with open('/workspace/Compass_NeyBackes_Robot/python_exercicios_dados/arquivos_auxiliares/compeonato.json') as json_normal:
     jsonManipulavel = json.load(json_normal)
    return jsonManipulavel

#armazenando a leitura do arquivo em uma variável
jsonRetornado = retornarJson()


#utlizando o laço for para imprimir as chaves
for keys in jsonRetornado:
    pprint.pprint(keys)


