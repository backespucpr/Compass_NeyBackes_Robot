#- - Printe o nome do Ator que ganhou o Oscar em 1993


#importando a bliblioteca pandas para trabalhar com o arquivo csv
import pandas as pd

#guardando o csv na variavel df (dataframe)
df = pd.read_csv('/workspace/Compass_NeyBackes_Robot/python_exercicios_dados/arquivos_auxiliares/arquivo.csv')

#da mesma forma que foi feito na atividade anterior esta resposta está na coluna Name na linha 65
oscarVencedor = df['Name'][65]

#imprimindo nossa resposta
print(f'''Nome do ator que ganhou o Oscar em 1993 \n
O vencedor de 1993 foi {oscarVencedor}
''')

