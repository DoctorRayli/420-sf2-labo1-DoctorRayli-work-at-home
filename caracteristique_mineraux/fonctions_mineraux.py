from caracteristique_mineraux.mineral import Mineral
from caracteristique_mineraux.metal import Metal
from caracteristique_mineraux.gemme import Gemme
from caracteristique_mineraux.log_combat import LogCombat
from fonctions_generales.validation import validation_mineraux as valide_min
from fonctions_generales.validation import validation_entree_normale as valide_normal

def masse_volume(mineral:Mineral|Metal|Gemme, masse_ou_volume:int) -> str:

    '''
    Cette fonction calcul la masse selon le volume d'un minéral et vice-versa
    Elle reçoit le minéral en question et la décision de l'utilisateur (masse->volume ou volume->masse)
    Elle retourne un texte qui affiche le résultat du calcul
    '''

    if masse_ou_volume == 2:
        masse = float(input("Le minéral a une masse de: "))
        volume = Mineral.masse_a_volume(mineral, masse)

        return f"\nLe {mineral.get_nom()} a un volume de {volume:.3f}cm3 s'il a une masse de {masse:.3f}g"

    else:
        volume = float(input("Le minéral a un volume de: "))
        masse = Mineral.volume_a_masse(mineral, volume)

        return f"\nLe {mineral.get_nom()} a une masse de {masse:.3f}g s'il a un volume de {volume:.3f}cm3"
   
def choix_mineraux(entree_valide:bool, mineraux:list[Mineral|Metal|Gemme]) -> Mineral|Metal|Gemme:

    '''
    Cette fonction sert à choisir une minéral parmi celles qui sont existantes
    Elle reçoit la variable booléenne 'entree_valide' et la liste des minéraux
    Elle retourne le minéral qui à été choisi
    '''

    while entree_valide == False:
        mineral, entree_valide = valide_min(mineraux, input("\nQuel est le minéral que vous voulez choisir (veuillez inscrire le numéro du minéral): ").lower(), entree_valide)

    return mineral

def choix_metal(entree_valide:bool, mineraux:list[Mineral|Metal|Gemme]) -> Metal:
    
    '''
    Cette fonction sert à choisir un métal parmi ceux qui sont existants
    Elle reçoit la variable booléenne 'entree_valide' et la liste des minéraux
    Elle retourne le métal qui à été choisi
    '''

    while entree_valide == False:
        metal, entree_valide = valide_min(mineraux, input("\nQuel est le métal que vous voulez choisir (veuillez inscrire le numéro du métal): ").lower(), entree_valide, "métal")        

    return metal

def voir_combat(entree_valide:bool, log_combat:list[LogCombat]) -> str:

    '''
    Cette fonction permet d'afficher les résultats des combats précédents (un nombre que l'utilisateur décide)
    Elle reçoit la liste des combats précédents
    Elle retourne un texte listant le résultat des combats que l'utilisateur veut voir
    '''

    if Mineral.nb_combat == 0:
        return f"\nIl n'y a pas eu de combats encore"
    
    while entree_valide == False:
        text = ""
        nombre_a_voir = int(valide_normal("6"))

        if 1 <= nombre_a_voir <= Mineral.nb_combat:
            for x in range(Mineral.nb_combat - 1, Mineral.nb_combat - nombre_a_voir - 1, -1):
                text += f"\nCombat {x + 1}: {str(log_combat[(x)])}"
            
            entree_valide = True

        else:
            text = "\nCe nombre est invalide, veuillez réessayer"

    return text
