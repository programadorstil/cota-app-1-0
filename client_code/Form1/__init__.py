from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.http
'''This is a simple example application created by me using Anvil, using the requests API
with response to currency quote, with text input and click action button.
'''

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

    # Any code you write here will run before the form opens.
  def button_1_click(self, **event_args):
    selecao1 = self.drop_down_1.selected_value
    selecao2 = self.drop_down_2.selected_value
    site = "https://economia.awesomeapi.com.br/last/"
    equal = selecao1 == selecao2
    if equal:
      alert("dropdows is equal")
    else:
      urlcomplete = site + selecao1 + "-" + selecao2
      print(urlcomplete)
      if selecao2 == 'USD':
        simbol = "Dollar(s)"
      elif selecao2 == 'BRL':
        simbol = "Reais"
      elif selecao2 == 'EUR':
        simbol = "Euro(s)"
      elif selecao2 == 'BTC':
        simbol = "Bitcoin(s)"
      elif selecao2 == 'ETH':
        simbol = "Ethereum"
      elif selecao2 == 'XRP':
        simbol = "Riplle(s)"
      elif selecao2 == 'DOGE':
        simbol = "Dogecoin(s)"
        
      #require API 
      requisicao = anvil.http.request(urlcomplete, method="GET", json=True)

      join = selecao1+selecao2

      cotacao = requisicao[join]['bid']
      txt = "A cotação de " + selecao1 + " para " + selecao2 + " é " +cotacao +" "+simbol 
      self.label_1.text = txt
    
    
    
    
    
    
  
 




 
        
    

  
 
    
    
     



  


