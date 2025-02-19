from caracteristique_mineraux.mineral import Mineral

class Collection:

    '''Cette classe décrit une collection selon son nom, son propriétaire et sa liste de minéraux'''

    def __init__(self, mineraux:list, proprietaire:str, nom:str):

        '''
        Fonction qui sert à construire de nouveux objets de classe Collection.
        Il assigne les attributs: nom, propriétaire et minéraux aux objets qui sont stockés dans la base de données
        '''

        self.__mineraux = mineraux
        self.__proprietaire = proprietaire
        self.__nom = nom

    def __str__(self):
        
        '''
        Fonction qui retourne une description détaillée d'une collection au choix (nom, propriétaire et minéraux)
        Il averti l'utilisateur si la collection contient un minéral radioactif
        Il retourne un texte (la description détaillée)
        '''

        nb_element_radioactif = 0

        text = f"\nLa collection {self.__nom} appartient à {self.__proprietaire} et elle contient les minéraux: "
        for x in self.__mineraux:
            text += f"Mineral № {x.get_numero()}: {x.get_nom()}, "

        for x in self.__mineraux:
            if x.get_radioactivite() == True:
                nb_element_radioactif += 1
               
        if nb_element_radioactif > 0:
            text += f"\n========== DANGER! PRÉSENCE DE {nb_element_radioactif} ÉLÉMENTS RADIOACTIFS =========="

        return text

    def get_mineraux(self):

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut minéraux d'un objet Collection
        Il retourne la liste de minéraux de la collection
        '''

        return self.__mineraux
   
    def get_proprietaire(self):

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut propriétaire d'un objet Collection
        Il retourne le nom du propriétaire de la collection
        '''

        return self.__proprietaire
   
    def get_nom(self):

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut nom d'un objet Collection
        Il retourne le nom de la collection
        '''

        return self.__nom

    def ajout_de_mineral(self, mineral) -> str:

        '''
        Fonction permettant d'ajouter un minéral dans une collection au choix
        Il ajoute le minéral à l'attribut minéraux (une liste)

        Il reçoit le minéral à ajouter
        Il retourne un texte signalant que le minéral à été ajouté ou qu'il est déjà présent dans la collection
        '''
    
        if mineral not in self.__mineraux:
            self.__mineraux.append(mineral)
            return f"Le {mineral.get_nom()} a été ajouté à la collection {self.__nom}."
       
        else:
            return f"Le {mineral.get_nom()} est déjà présent dans la collection {self.__nom}"

    def creation(collections:list, nom:str, proprietaire:str, mineraux:list) -> list:

        '''
        Fonction permettant à l'utilisateur de créer sa propre collection en appelant la fonction __init__
        Il l'ajoute à la liste de collection existante

        Il reçoit tous les données nécéssaire pour la création d'une collection (nom, propriétaire et liste de minéraux)
        Il retourne la liste de collections modifiée
        '''

        collections.append(Collection(mineraux, proprietaire, nom))
        return collections
   
    def plus_grande_puissance(self):

        '''
        Cette fonction permet à l'utilisateur de déterminer le minéral le plus puissant d'une collection
        Il retourne une phrase déclarant le minéral le plus puissant
        '''

        plus_puissant = self.__mineraux[0]

        for x in range(len(self.__mineraux) - 1):
            gagnant, perdant, score_gagnant, score_perdant, texte = Mineral.combat_de_mineraux(plus_puissant, self.__mineraux[x])
            plus_puissant = gagnant

        return f"\nLe {plus_puissant.get_nom()} est le minéral le plus puissant dans la collection {self.__nom}"
   