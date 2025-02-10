from caracteristique_mineraux.mineral import Mineral

class LogCombat:

    '''Cette classe décrit un combat selon le gagnant, le perdant et le type de victoire'''

    def __init__(self, gagnant:Mineral, perdant:Mineral, type_de_victoire:str):

        '''
        Fonction qui sert à construire de nouveux objets de classe LogCombat.
        Il assigne les attributs: gagnant, perdant et type de victoire aux objets qui sont stockés dans la base de données
        '''

        self.__gagnant = gagnant
        self.__perdant = perdant
        self.__type_de_victoire = type_de_victoire

    def __str__(self):
        return self.afficher()

    def afficher(self) -> str:

        '''
        Cette fonction permet d'afficher la description d'un combat: le gagnant, perdant et le type de victoire
        Elle retourne la description du combat sous forme de texte
        '''

        if self.__type_de_victoire != "égalité":
            text = f"Le {self.__gagnant.get_nom()} a battu le {self.__perdant.get_nom()} car il est {self.__type_de_victoire}"

        else:
            text =  f"Il y a une égalité entre le {self.__gagnant.get_nom()} et le {self.__perdant.get_nom()}"

        return text
   