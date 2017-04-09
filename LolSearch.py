import requests
import time

def titulo():
	print('''\033[31m
	 _       _                         _    
	| |     | |                       | |    
	| | ___ | |___  ___  __ _ _ __ ___| |__  
	| |/ _ \| / __|/ _ \/ _` | '__/ __| '_ \ 
	| | (_) | \__ \  __/ (_| | | | (__| | | |
	|_|\___/|_|___/\___|\__,_|_|  \___|_| |_|
	\033[31m
		\033[37mBy: Felipe Tesao\033[37m
''')

def busca(nome,regiao):
	url='https://'+regiao+'.op.gg/summoner/userName='+nome
	
	try:
		req=requests.get(url)

		elo=req.text
		elo=elo.split('<span class="tierRank">',maxsplit=1)
		del elo[0]
		elo="".join(elo)
		elo=elo.split(r'</span>',maxsplit=1)
	
	
		del elo[1]
		elo="".join(elo)

		#==============================#

		vitoria=req.text
		vitoria=vitoria.split(r'<div class="Text">')
		del vitoria[0]
		vitoria = "".join(vitoria)
		vitoria=vitoria.split(r'</div>',maxsplit=1)
		del vitoria[1]
		vitoria="".join(vitoria)
	

		#==============================#

		champ=req.text
		champ=champ.split(r'<div class="ChampionName" title="',maxsplit=1)
		del champ[0]
		champ = "".join(champ)
		champ=champ.split(r'">',maxsplit=1)
		del champ[1]
		champ="".join(champ)
	
		#==============================#

		amigo=req.text
		amigo=amigo.split(r'<a href="//br.op.gg/summoner/userName=',maxsplit=1)
		del amigo[0]
		amigo = "".join(amigo)

		amigo=amigo.split(r'" class="Link">',maxsplit=1)
		del amigo[0]
		amigo = "".join(amigo)
	
		amigo=amigo.split(r'</a>',maxsplit=1)
		del amigo[1]
		amigo="".join(amigo)
	
		print('''
	#====================================================#		
		Nick: %s
		
		Elo: %s
		
		Porcentagem de vitoria: %s
		
		Campeao mais jogado: %s
					
		Amigo mais jogado: %s
	#====================================================#
			'''%(nome,elo,vitoria,champ,amigo))
	
	except:
		print("Erro de conexao ou jogador nao encontrado!")


while True:
	titulo()
	print("Regioes:\n\n 	br (Brasil), jp (Japao), euw (Europa oeste)\n 	eune (Europa nordica e Leste), oce (Oceania)\n 	na (America do norte), ru (Russia)\n 		www (Coreia)\n\n")
	regiao=input("Digite a regiao do jogador: ")
	
	if(regiao==""):
		print("Por favor digite Uma regiao!")
		break

	nome=input("Digite o nick do jogador: ")
	
	
	if(nome==""):
		print("Por favor digite um Nick de jogador!")
		break

	busca(nome,regiao)
	print("\n Espere 4 segundos!")
	time.sleep(4)
