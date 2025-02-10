from caracteristique_collections.collection import Collection
from fonctions_generales.validation import validation_collections as valide_col

def choix_collection(entree_valide:bool, collections:list) -> Collection:

    '''
    Cette fonction sert à choisir une collection parmi celles qui sont existantes
    Elle reçoit la variable booléenne 'entree_valide' et la liste des collections
    Elle retourne la collection qui à été choisi
    '''

    while entree_valide == False:
        print("\nVeuillez choisir parmi les collections suivantes:")
        for x in collections:
            print(f"- {x.get_nom()}")

        collection, entree_valide = valide_col(collections, input("Votre choix: "), entree_valide)

    return collection

def collect_information_collection(mineraux:list):

    '''
    Cette fonction perment la récolte des informations nécéssaires à la création d'une collection
    Elle reçoit la liste de minéraux
    Elle retourne les informations nécéssaires à la création d'une collection (nom capitalisé, propriétaire et liste de minéraux)
    '''

    nom = input("Quel est le nom de la collection: ").split()
    nom_capitalise = ""
    for x in nom:
        nom_capitalise += f"{x.capitalize()} "

    proprietaire = input("Qui possède la collection: ")
    mineraux_collection = []

    lst_mineraux = input("Quels mineraux voulez-vous ajouter à cette collection (veuillez inscrire les numéros de tous les minéraux): ").replace(",", " ").split()
               
    for x in lst_mineraux:
        if x.isalpha() == False:
            if int(x) < len(mineraux) - 1 and mineraux[int(x) - 1] not in mineraux_collection:
                mineraux_collection.append(mineraux[int(x) - 1])

    return nom_capitalise, proprietaire, mineraux_collection
