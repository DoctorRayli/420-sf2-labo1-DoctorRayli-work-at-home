from caracteristique_mineraux.mineral import Mineral
from caracteristique_mineraux.metal import Metal
from caracteristique_mineraux.gemme import Gemme

class LogCombat:

    '''Cette classe décrit un combat selon le gagnant, le perdant et le type de victoire'''

    def __init__(self, gagnant:Mineral|Metal|Gemme, perdant:Mineral|Metal|Gemme, point_gagnant:int, point_perdant:int):

        '''
        Fonction qui sert à construire de nouveux objets de classe LogCombat.
        Il assigne les attributs: gagnant, perdant et type de victoire aux objets qui sont stockés dans la base de données
        '''

        self.__gagnant = gagnant
        self.__perdant = perdant
        self.__point_gagnant = point_gagnant
        self.__point_perdant = point_perdant

    def __str__(self) -> str:
        
        '''
        Cette fonction permet redéfini la méthode spéciale 'str' qui permet maintenant d'afficher la description d'un combat: le gagnant, perdant et le type de victoire
        Elle retourne la description du combat sous forme de texte
        '''

        if self.__point_gagnant == self.__point_perdant:
            text =  f"Il y a une égalité entre le {self.__gagnant.get_nom()} et le {self.__perdant.get_nom()} à {self.__point_gagnant:.3f}"

        else:
            text = f"Le {self.__gagnant.get_nom()} a battu le {self.__perdant.get_nom()} car il a un pointage plus élevé de {self.__point_gagnant - self.__point_perdant:.3f}"

        return text
   