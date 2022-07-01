#- - Usando Pandas, procure por um dado específico (da sua escolha) e printe somente o mesmo utilizando o CSV.


#importando a bliblioteca pandas para trabalhar com o arquivo csv
import pandas as pd

#guardando o csv na variavel df (dataframe)
df = pd.read_csv('/workspace/Compass_NeyBackes_Robot/python_exercicios_dados/arquivos_auxiliares/arquivo.csv')

#Para ficar mais interessante vamos nos fazer uma questão:
#Quem foi o vencendo do oscar de 2012? E qual foi o filme vencedor?

#estes dados estão na linha 84 na coluna Name e Movie, portanto, precisamos acessar essa informações
oscarVencedor = df['Name'][84]
filmeVencedor = df['Movie'][84]

#imprimindo nossa resposta
print(f'''Quem foi o vencedor do oscar de 2012? \n
O vencedor de 2012 foi {oscarVencedor} por sua atuação no filme {filmeVencedor}
''')