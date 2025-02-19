from caracteristique_alliages.alliage import Alliage
from fonctions_generales.validation import validation_mineraux as valide_min
from fonctions_generales.validation import validation_alliage as valide_all

def choix_alliage(entree_valide:bool, alliages:list[Alliage]) -> Alliage:

    '''
    Cette fonction sert à choisir une minéral parmi celles qui sont existantes
    Elle reçoit la variable booléenne 'entree_valide' et la liste des minéraux
    Elle retourne le minéral qui à été choisi
    '''

    while entree_valide == False:
        alliage, entree_valide = valide_all(alliages, input("\nQuel est l'alliage que vous voulez choisir (veuillez inscrire le numéro de l'alliage): ").lower(), entree_valide)

    return alliage

def choix_metal(entree_valide:bool, mineraux:list, alliage="", soustraire:bool=False):
    
    '''
    Cette fonction sert à choisir une minéral parmi celles qui sont existantes
    Elle reçoit la variable booléenne 'entree_valide' et la liste des minéraux
    Elle retourne le minéral qui à été choisi
    '''

    while entree_valide == False:
        metal, entree_valide = valide_min(mineraux, input("\nQuel est le métal que vous voulez choisir (veuillez inscrire le numéro du métal): ").lower(), entree_valide, "métal")        

    return metal
