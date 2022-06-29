#Abra o arquivo CSV com pandas e guarde em uma variável de sua
#escolha e printe o conteúdo no terminal

#importando a bliblioteca pandas para trabalhar com o arquivo csv
import pandas as pd

#guardando o csv na variavel df (dataframe)
df = pd.read_csv('/workspace/Compass_NeyBackes_Robot/python_exercicios_dados/arquivos_auxiliares/arquivo.csv')

#imprimindo na tela 
print(df) 

