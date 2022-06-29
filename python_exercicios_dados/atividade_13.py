#-3- Crie mais uma coluna em tempo de execução juntando os dadosmovie e year

#importando a bliblioteca pandas para trabalhar com o arquivo csv
import pandas as pd

#guardando o csv na variavel df (dataframe)
df = pd.read_csv('/workspace/Compass_NeyBackes_Robot/python_exercicios_dados/arquivos_auxiliares/arquivo.csv')


#criando uma nova coluna e concatenando com as informações de Movie e Year
df["Execution Time"] = df["Movie"] + str(df["Year"])


print(df)