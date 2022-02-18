# -*-coding:Latin-1 -*
import os

#DEBUT
print("**********************************************************************************")
print("PROGRAMME PERMETTANT DE \nRECONNAITRE SI UNE ANNEE EST\n BISSEXTILE OU PAS")
print("**********************************************************************************")
print("\n")
print("\n")
annee = int(input("Veuillez saisir une année : "))
if(annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0)):
	print(annee, "est une année bissextile!")
else:
	print(annee, "n'est pas une année bissextile.")
#FIN	
	
os.system("pause")
