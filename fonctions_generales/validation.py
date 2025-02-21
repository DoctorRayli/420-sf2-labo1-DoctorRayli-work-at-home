import re
from caracteristique_mineraux.mineral import Mineral
from caracteristique_mineraux.gemme import Gemme
from caracteristique_mineraux.metal import Metal
from caracteristique_collections.collection import Collection
from caracteristique_alliages.alliage import Alliage

def validation_entree_normale(choix:str, metal_choix="", alliage_choix="") -> tuple[str, bool]|str|int:

    '''
    Cette fonction les entrées de l'utilisateur aux questions normales soient valides
    Elle reçoit le choix de l'utilisateur (au menu) et le métal et l'alliage choisie si nécésssire
    Elle retourne la réponse de l'utilisateur et une valeur booléenne qui affirme ou non si la réponse est valide
    '''
    
    match choix:
        case "3":
            texte = input("\nVoulez-vous calculer sa masse à partir du volume (1) ou calculer le volume à partir de la masse (2)? ")
            validation = r"\b1|2\b"
            trouver = re.search(validation, texte)
            if trouver:
                return trouver[0], True
            
            else:
                print("\nEntrée invalide, veuillez choisir 1 ou 2")
                return texte, False
            
        case "6":
            texte = input(f"\nCombien des combats précédents voulez-vous voir (maximum de {Mineral.nb_combat})? ")
            validation = r"\b[0-9]+\b"
            trouver = re.search(validation, texte)
            if trouver:
                return trouver[0]
            
            else:
                print("\nEntrée invalide, veuillez rentrer un nombre de combats valide")
                return Mineral.nb_combat + 1
            
        case "13":
            texte = input(f"\nCombien de grammes du métal voulez-vous ajouter à l'alliage? ")
            validation = r"\b[0-9]+\b"
            trouver = re.search(validation, texte)
            if trouver:
                return trouver[0], True

            print("\nEntrée invalide, veuillez rentrer un nombre de gramme")
            return texte, False

        case "14":
            texte = input(f"\nCombien de grammes du {metal_choix.get_nom()} voulez-vous soustraire à l'alliage? (maximum {alliage_choix.get_metaux()[metal_choix]}g): ")
            validation = r"\b[0-9]+\b"
            trouver = re.search(validation, texte)
            if trouver and  0 < int(trouver[0]) <= alliage_choix.get_metaux()[metal_choix]:
                return trouver[0], True

            print("\nEntrée invalide, veuillez rentrer un nombre de gramme adéquat")
            return texte, False
        
        case "15":
            texte = input(f"\nCombien de grammes du {metal_choix.get_nom()} voulez-vous ajouter à l'alliage? ")
            validation = r"\b[0-9]+\b"
            trouver = re.search(validation, texte)
            if trouver:
                return trouver[0], True

            print("\nEntrée invalide, veuillez rentrer un nombre de gramme")
            return texte, False

        case "16":
            texte = input("\nVoulez-vous choisir un métal (1) ou un alliage (2)? ")
            validation = r"\b1|2\b"
            trouver = re.search(validation, texte)
            if trouver:
                return trouver[0], True
            
            else:
                print("\nEntrée invalide, veuillez choisir 1 ou 2")
                return texte, False
        
def choix_utilisateur(entree_valide:bool, choix:str, metal_choix="", alliage_choix="") -> str|int:

    '''
    Cette fonction s'assure que l'utilissateur rentre une réponse valide (boucle la fonction ci-dessus)
    Elle reçoit la valeur booléenne 'entree_valide', le choix de l'utilisateur (au menu) et le métal et l'alliage choisi si nécéssaire
    Elle retourne la réponse de l'utilisateur
    '''

    while entree_valide == False:
        texte, entree_valide = validation_entree_normale(choix, metal_choix, alliage_choix)

    return texte

def validation_mineraux(mineraux:list[Mineral|Metal|Gemme], mineral:str, entree_valide:bool, type_mineraux:str="") -> tuple[str|Mineral|Metal|Gemme, bool]:

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

def validation_collections(collections:list[Collection], collection:str, entree_valide:bool) -> tuple[str|Collection, bool]:

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

def validation_alliage(alliages:list[Alliage], alliage:str, entree_valide:bool) -> tuple[str|Alliage, bool]:
    
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
        continuer = re.findall(recherche, input("Votre entrée est invalide, voulez-vous réessayer (1) ou voir la liste des alliages (2)? "))
        alliage_choisi = ""

        if  "2" in continuer:
            print(Alliage.liste_alliages(alliages))

    return alliage_choisi, entree_valide
       