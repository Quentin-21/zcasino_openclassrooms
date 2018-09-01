# -*-coding:utf-8 -*

# JEU DE LA ROULETTE version console

"""
REGLE :
	1. Choisir num entre 0-49 (= numero_roulette)
	2. Choisir une somme à misé (= somme)
	3. Roue tourne + lancé de la bille:
		-> 50 cases:
			-> pairs => noir
			-> impairs => rouge
		la bille tombe dans une case
	4. SI numero_roulette = gagnant ==> joueur recoit 3 x somme
	5. SINON SI numero_roulette meme couleur numero gagnant 
		(ex: si numero gagnant = pair et numero_roulette = pair ==> joueur recoit 0.5 x somme)
	6. SINON argent perdu -somme misée

"""

# MODULE
import os # Module interagissant avec le systeme
from math import ceil # Module permettant d'effectuer des operations math
from random import randrange # fonction permettant de choisir un nombre au hazard

# ESTHETIQUE
os.system("clear")

print("")
print("	$$$$$$$$\\  $$$$$$\\                      $$\\")                     
print("	\\____$$  |$$  __$$\\                     \\__|")                    
print("	    $$  / $$ /  \\__| $$$$$$\\   $$$$$$$\\ $$\\ $$$$$$$\\   $$$$$$\\")  
print("	   $$  /  $$ |       \\____$$\\ $$  _____|$$ |$$  __$$\\ $$  __$$\\") 
print("	  $$  /   $$ |       $$$$$$$ |\\$$$$$$\\  $$ |$$ |  $$ |$$ /  $$ |")
print("	 $$  /    $$ |  $$\\ $$  __$$ | \\____$$\\ $$ |$$ |  $$ |$$ |  $$ |")
print("	$$$$$$$$\\ \\$$$$$$  |\\$$$$$$$ |$$$$$$$  |$$ |$$ |  $$ |\\$$$$$$  |")
print("	\\________| \\______/  \\_______|\\_______/ \\__|\\__|  \\__| \\______/")
print(" \n Bienvenue dans le jeu de la roulette. \nPour commencer vous disposez d'une somme initiale de 1000$. \nVous pourrez quitter le jeu dès que vous le voudrez,\ntapez seulement sur q ...")
print(" \n")

compte = 1000 # Ceci represente la somme de départ 

while 1:
	# Premiere question
	numero_mise = input("\nChoisissez un numéro (0-49) : ")
	try:
		numero_mise = int(numero_mise)

		assert numero_mise >= 0
		assert numero_mise <= 49

		# Deuxieme question
		somme_mise = input("Pour Combien misez-vous sur ce nombre : ")
		try:
			somme_mise = int(somme_mise)

			assert somme_mise < 0
			assert somme_mise > compte

		except AssertionError:
			if somme_mise > compte:
				print("Vous n'avez pas assez d'argent")
				continue
			elif somme_mise < 0:
				print("Vous n'avez plus d'argent pour continuer")
				continue
		except:
			print("Veuillez saisir un nombre correct")
			continue

	except AssertionError:
		if numero_mise <= 0 or numero_mise >= 49:
			print("Veuillez saisir un nombre entre 0 et 49")
			continue
	except:
		print("Veuillez saisir un nombre correct")
		continue
	else:
		# roulette
		nb_hasard = randrange(50)
		print("\nLa roulette tourne... et la bille tombe sur le numéro : ", nb_hasard)

		if numero_mise == nb_hasard:
			# Joueur recoit 3x somme_mise
			print("Bravo ! La bille est tombée sur le numéro que vous avez misé, \nvous recevez ",ceil(somme_mise * 3), "$.")
			compte = ceil(compte + (somme_mise * 3))
			print("Compte : ",compte, "$.")

		elif (nb_hasard%2 == 0 and numero_mise%2 == 0) or (nb_hasard%2 != 0 and numero_mise%2 != 0): 
			# Joueur recoit 0.5x somme_mise
			print("La bille est tombée sur la même couleur que le numéro que vous avez misé, \nvous recevez ",ceil(somme_mise * 0.5), "$.")
			compte = ceil(compte + (somme_mise * 0.5))
			print("Compte : ",compte, "$.")

		else:
			compte = ceil(compte - somme_mise)
			# Joueur perd argent mise
			print("Dommage, vous avez perdu ",ceil(somme_mise), "$.")
			print("Compte : ",compte, "$.")

	finally:
		saisie = input("\nVoulez-vous continuer ? (o/n) ")
		if saisie == "o":
			pass
		else:
			break
	
