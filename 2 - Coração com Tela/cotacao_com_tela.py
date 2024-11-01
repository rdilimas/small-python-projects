
import requests
from tkinter import * 

def obter_contacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro.: {cotacao_euro}
    BTC..: {cotacao_btc}
    '''

    texto_cotacoes["text"] = texto

janela = Tk()
janela.title("Sistema de Cotação")

texto_orientacao = Label(janela, text="Click no botão para exibir a Cotação das moedas")
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Buscar Cotações do Euro/Dólar/BTC", command=obter_contacoes)
botao.grid(column=0, row=1)

texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=0, row=2)

janela.mainloop()
