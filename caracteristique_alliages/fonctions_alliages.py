import random
import re
from caracteristique_mineraux.metal import Metal
from caracteristique_mineraux.mineral import Mineral
from caracteristique_mineraux.gemme import Gemme
from caracteristique_alliages.alliage import Alliage
from caracteristique_mineraux import fonctions_mineraux
from fonctions_generales import validation

def choix_alliage(entree_valide:bool, alliages:list[Alliage]) -> Alliage:

    '''
    Cette fonction sert à choisir une minéral parmi celles qui sont existantes
    Elle reçoit la variable booléenne 'entree_valide' et la liste des allaiges
    Elle retourne le minéral qui à été choisi
    '''

    while entree_valide == False:
        alliage, entree_valide = validation.validation_alliage(alliages, input("\nQuel est l'alliage que vous voulez choisir (veuillez inscrire le numéro de l'alliage): ").lower(), entree_valide)

    return alliage

def choix_combattant(entree_valide:bool, mineraux:list[Mineral|Metal|Gemme], alliages:list[Alliage], choix:str, hasard=False) -> Alliage|Metal:

    '''
    Cette fonction sert à choisir un combattant d'un combat alliage-métal
    Elle reçoit la variable booléenne 'entree_valide', la liste des minéraux, la liste des alliages, le choix de l'utilisateur(menu principale) et le choix de choisir au hasard
    Elle retourne l'alliage ou le métal qui à été choisi
    '''

    if hasard == False:
        texte = validation.choix_utilisateur(entree_valide, choix)

        if texte == "1":
            metal = fonctions_mineraux.choix_metal(entree_valide, mineraux)
            return metal
            
        else:
            alliage = choix_alliage(entree_valide, alliages)
            return alliage
        
    else:
        if random.randint(1,2) == 1:
            return alliages[random.randint(0, len(alliages) - 1)]

        else:
            return mineraux[random.randint(25,42)]
        
def collect_information_alliage(mineraux:list[Mineral|Metal|Gemme]) -> tuple[str, dict[Metal, float]]:

    '''
    Cette fonction perment la récolte des informations nécéssaires à la création d'un alliage
    Elle reçoit la liste de minéraux
    Elle retourne les informations nécéssaires à la création d'une collection (nom capitalisé et dictionnaire métaux-masse)
    '''

    nom = input("Quel est le nom de le l'alliage: ").split()
    nom_capitalise = ""
    for x in nom:
        nom_capitalise += f"{x.capitalize()} "

    metaux_alliage = {}

    while len(metaux_alliage) == 0:
        print(f"Parmi les métaux suivants: {Metal.liste_metaux(mineraux)}")
        lst_metaux = input("Quels métaux voulez-vous ajouter à cet alliage (veuillez inscrire les numéros de tous les minéraux): ").replace(",", " ").split()     
        for x in lst_metaux:
            if x.isalpha() == False:
                if 26 <= int(x) <= 43 and mineraux[int(x) - 1] not in metaux_alliage.keys():
                    masse = input(f"Combien de grammes de {mineraux[int(x) - 1].get_nom()} voulez-vous ajouter à votre alliage? ")
                    validite = re.search(r"[0-9]+", masse)

                    if validite:
                        if validite[0].isnumeric() == True:
                            metaux_alliage[mineraux[int(x) - 1]] = int(validite[0])

                        else:
                            print(f"Entrée invalide, nous allons considérer que vous avez mis 0g de {mineraux[int(x) - 1].get_nom()}")

                    else:
                        print(f"Entrée invalide, nous allons considérer que vous avez mis 0g de {mineraux[int(x) - 1].get_nom()}")
        
        if len(metaux_alliage) == 0:
            print(f"\nEntrez invalide, vous devez choisir au moins un métal parmi ceux-ci:\n{Metal.liste_metaux(mineraux)}")

    return nom_capitalise, metaux_alliage
