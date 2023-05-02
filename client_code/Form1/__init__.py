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
    
    
   #requisição 
    requisicao = anvil.http.request("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL", method="GET", json=True)
    
    cotacao_dolar = requisicao['USDBRL']['bid']
    cotacao_euro = requisicao['EURBRL']['bid']
    cotacao_btc = requisicao['BTCBRL']['bid']
    #verificação do que foi digitado
    if txt == "usd" or txt == "USD":
      self.label_1.text = " A cotaçõa atual do " + txt + " é  R$ "+ cotacao_dolar
    elif txt == "eur" or txt == "EUR":
      self.label_1.text = " A cotaçõa atual do  " + txt + " é  R$ "+ cotacao_euro
    elif txt == "btc" or txt == "BTC":
      self.label_1.text = " A cotaçõa atual do  " + txt + " é  R$ "+ cotacao_btc
    else:
      alert("Opção invalida,digite USD,EUR or BTC")
        
    

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass


 
    
    
     



  


