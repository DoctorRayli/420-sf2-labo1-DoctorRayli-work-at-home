import re
from caracteristique_mineraux.mineral import Mineral
from caracteristique_mineraux.gemme import Gemme
from caracteristique_mineraux.metal import Metal
from caracteristique_collections.collection import Collection
from caracteristique_alliages.alliage import Alliage

def validation_entree_normale(texte:str, choix:str):
    
    match choix:
        case "3":
            validation = r"\b1|2\b"
            trouver = re.search(validation, texte)
            if trouver:
                return trouver[0], True
            
            else:
                return texte, False
            
        case "6":
            validation = r"\b[1-9]+\b"
            trouver = re.search(validation, texte)
            if trouver:
                return trouver[0]
            
            else:
                return Mineral.nb_combat + 1
            
        case "13":
            validation = r"\b[0-9]+\b"
            trouver = re.search(validation, texte)
            if trouver:
                return trouver[0], True
            
            else:
                return texte, False

def validation_mineraux(mineraux:list, mineral:str, entree_valide:bool, type_mineraux:str=""):

    '''
    Cette fonction permet de valider que le minéral choisi par l'utilisateur fait parti de la liste existante de minéraux
    Elle reçoit la liste de minéraux, la demande de l'utilisateur et la valeur booléenne 'entree_valide'
    Elle retourne le minéral choisi et la variable 'entree_valide'
    '''

    text = ""
    recherche = r"\b[0-9]{1,2}\b"
   
    for x in mineral.split():
        text += f"{x.capitalize()} "

    if type_mineraux == "métal":
        for x in mineraux:
            if (x.get_nom() in text or str(x.get_numero()) in mineral.split()) and type(x) == Metal:
                mineral_choisi = x
                entree_valide = True

        if entree_valide == False:
            continuer = re.findall(recherche, input("Votre entrée est invalide, voulez-vous réessayer (1) ou voir la liste des métaux (2)? "))
            mineral_choisi = ""

            if  "2" in continuer:
                print(Metal.liste_metaux(mineraux))

    elif type_mineraux == "gemme":
        for x in mineraux:
            if (x.get_nom() in text or str(x.get_numero()) in mineral.split()) and type(x) == Gemme:
                mineral_choisi = x
                entree_valide = True

        if entree_valide == False:
            continuer = re.findall(recherche, input("Votre entrée est invalide, voulez-vous réessayer (1) ou voir la liste des gemmes (2)? "))
            mineral_choisi = ""

            if  "2" in continuer:
                print(Gemme.liste_gemme(mineraux))

    else:
        for x in mineraux:
            if x.get_nom() in text or str(x.get_numero()) in mineral.split():
                mineral_choisi = x
                entree_valide = True

        if entree_valide == False:
            continuer = re.findall(recherche, input("Votre entrée est invalide, voulez-vous réessayer (1) ou voir la liste des minéraux (2)? "))
            mineral_choisi = ""

            if  "2" in continuer:
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
        collection_choisie = ""
        print("Entrée invalide, veuillez réessayer")

    return collection_choisie, entree_valide

def validation_alliage(alliages:list[Alliage], alliage:str, entree_valide:bool):
    
    '''
    Cette fonction permet de valider que le minéral choisi par l'utilisateur fait parti de la liste existante de minéraux
    Elle reçoit la liste de minéraux, la demande de l'utilisateur et la valeur booléenne 'entree_valide'
    Elle retourne le minéral choisi et la variable 'entree_valide'
    '''

    text = ""
    recherche = r"\b[0-9]{1,2}\b"
   
    for x in alliage.split():
        text += f"{x.capitalize()} "

    for x in alliages:
        if x.get_nom() in text or str(x.get_numero()) in alliage.split():
            alliage_choisi = x
            entree_valide = True

    if entree_valide == False:
        continuer = re.findall(recherche, input("Votre entrée est invalide, voulez-vous réessayer (1) ou voir la liste des minéraux (2)? "))
        alliage_choisi = ""

        if  "2" in continuer:
            print(Alliage.liste_alliages(alliages))

    return alliage_choisi, entree_valide
       