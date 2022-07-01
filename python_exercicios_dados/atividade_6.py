 #Faça com que o programa printe apenas os primeiros dados dentro de
 #edicao_atual, fase_atual, rodada_atual usando o JSON 2

#importando a biblioteca json
import json
#função como o metodo open para a leitura do arquivo json
def retornarJson():
    #precisei alterar como o caminho de acesso já que estou trabalhando com vscode na nuvem(gitpod) direto do próprio github.
    with open('/workspace/Compass_NeyBackes_Robot/python_exercicios_dados/arquivos_auxiliares/compeonato.json') as json_normal:
     jsonManipulavel = json.load(json_normal)
    return jsonManipulavel

#armazenando a leitura do arquivo em uma variável
jsonRetornado = retornarJson()
#guardando dados do time visitante



#encontrei um solução interessante no stackoverflow para coletar informações de dicionários transformando em listas
#assim eu consigo acessar quaquer dado facilmente pelo indice

#coletando as informações em variáveis
edicaoAtual = list(jsonRetornado['edicao_atual'].items())[0]
faseAtual = list(jsonRetornado['fase_atual'].items())[0]
rodadaAtual = list(jsonRetornado['rodada_atual'].items())[0]
#imprimindo na telas as informações
print(f'''O primeiro dado dentro da Edição atual é {edicaoAtual}
O primeiro dados dentro da Fase atual é {faseAtual}
O primeiro dado dentro da Fase atual é {rodadaAtual}
''')