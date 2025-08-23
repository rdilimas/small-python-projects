import pandas as pd
import plotly.express as px


tabela = pd.read_csv("C:/small-python-projects/10 - Dados/base_estudo.csv")
print(tabela)

correlacao = tabela.corr()

print(correlacao)

grafico = px.imshow(correlacao, text_auto=True, color_continuous_scale="Reds")

grafico.show()