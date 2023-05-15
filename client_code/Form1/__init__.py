from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.http
'''This is a simple example application created by me using kivyMD, using the requests API
with response to currency quote, with text input and click action button.
'''

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    
    txt = self.text_box_1.text
    txt = txt.upper()
    print(txt)
    
    
   #requisição 
    requisicao = anvil.http.request("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,ETH-BRL,XRP-BRL,DOGE-BRL", method="GET", json=True)
    
    cotacao_dolar = requisicao['USDBRL']['bid']
    cotacao_euro = requisicao['EURBRL']['bid']
    cotacao_btc = requisicao['BTCBRL']['bid']
    cotacao_eth = requisicao['ETHBRL']['bid']
    cotacao_xrp = requisicao['XRPBRL']['bid']
    cotacao_doge = requisicao['DOGEBRL']['bid']
    #verificação do que foi digitado
    if txt == "USD":
      self.label_1.text = " A cotaçõa atual do " + txt + " é  R$ "+ cotacao_dolar
    elif txt == "EUR":
      self.label_1.text = " A cotaçõa atual do  " + txt + " é  R$ "+ cotacao_euro
    elif txt == "BTC":
      self.label_1.text = " A cotaçõa atual do  " + txt + " é  R$ "+ cotacao_btc
    elif txt == "ETH":
      self.label_1.text = " A cotaçõa atual do  " + txt + " é  R$ "+ cotacao_eth
    elif txt == "XRP":
      self.label_1.text = " A cotaçõa atual do  " + txt + " é  R$ "+ cotacao_xrp  
    elif txt == "XRP":
      self.label_1.text = " A cotaçõa atual do  " + txt + " é  R$ "+ cotacao_xrp    
    elif txt == "DOGE":
      self.label_1.text = " A cotaçõa atual do  " + txt + " é  R$ "+ cotacao_doge    
    else:
      alert("Opção invalida!!\n\nPara moedas digite:\n USD ou EUR \n  Para Cripto,digite:\n BTC, ou ETH, ou XRP, ou DOGE ")
        
    

  def text_box_1_pressed_enter(self, **event_args):
    self.button_1_click()
    pass


 
    
    
     



  


