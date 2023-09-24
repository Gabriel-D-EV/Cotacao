import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    r["text"] = texto


janela = Tk()

janela.title("Cotações")
janela.geometry("180x180",)

to = Label(janela, text="clique para ver as cotações")
to.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Buscar Cotações", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)

r = Label(janela, text="...")
r.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()