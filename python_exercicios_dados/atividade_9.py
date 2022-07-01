#Usando Pandas, leia apenas os dados da coluna Age do CSV.


#importando a bliblioteca pandas para trabalhar com o arquivo csv
import pandas as pd

#guardando o csv na variavel df (dataframe)
df = pd.read_csv('/workspace/Compass_NeyBackes_Robot/python_exercicios_dados/arquivos_auxiliares/arquivo.csv')

#Guardando dados da coluna Age
colunaAge = df['Age']

#imprimindo na tela
print(colunaAge)
