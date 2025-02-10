from caracteristique_mineraux.mineral import Mineral
from caracteristique_collections.collection import Collection

def validation_mineraux(mineraux:list[Mineral], mineral:str, entree_valide:bool):

    '''
    Cette fonction permet de valider que le minéral choisi par l'utilisateur fait parti de la liste existante de minéraux
    Elle reçoit la liste de minéraux, la demande de l'utilisateur et la valeur booléenne 'entree_valide'
    Elle retourne le minéral choisi et la variable 'entree_valide'
    '''

    text = ""
   
    for x in mineral.split():
        text += f"{x.capitalize()} "
   
    for x in mineraux:
        if x.get_nom() in text or str(x.get_numero()) in mineral.split():
            mineral_choisi = x
            entree_valide = True

    if entree_valide == False:
        continuer = int(input("Votre entrée est invalide, voulez-vous réessayer (1) ou voir la liste des minéraux (2)? "))
        mineral_choisi = ""


        if continuer == 2:
            print(Mineral.liste_mineraux(mineraux))

    return mineral_choisi, entree_valide

def validation_collections(collections:list[Collection], collection:str, entree_valide:bool):

    '''
    Cette fonction permet de valider que la collection choisi par l'utilisateur fait parti de la liste existante de collections
    Elle reçoit la liste de collections, la demande de l'utilisateur et la valeur booléenne 'entree_valide'
    Elle retourne la collection choisi et la variable 'entree_valide'
    '''

    text = ""
   
    for x in collection.split():
        text += f"{x.capitalize()} "
   
    for x in collections:
        if x.get_nom() in text:
            collection_choisie = x
            entree_valide = True

    if entree_valide == False:
        print("Entrée invalide, veuillez réessayer")

    return collection_choisie, entree_valide

def validation_alliage():
    return
       