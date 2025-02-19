from caracteristique_mineraux.mineral import Mineral
from caracteristique_mineraux.couleur import CouleurRGB

'''Addon sur le laboratoire 1'''

class Metal(Mineral):

    ''''''

    def __init__(self, numero:int, nom:str, formule_chimique:str,  couleur:CouleurRGB, lustre:str, radioactivite:bool, durete:int, masse_volumique:float, conductivite:float, valeur:float):
        super().__init__(numero, nom, formule_chimique,  couleur, lustre, radioactivite, durete, masse_volumique)
        self.__conductivite = conductivite
        self.__valeur = valeur

    def get_conductivite(self):
        return self.__conductivite
    
    def get_valeur(self):
        return self.__valeur

    def __str__(self):
        text = super().__str__() 
        text += f"\nConductivité: {self.get_conductivite()}S/m \nValeur: {self.get_valeur()}$/kg \nScore: {self.score():.3f}"
        if self.get_radioactivite() == True:
            text += "\n========== DANGER! ÉLÉMENT RADIOACTIF =========="

        return text
    
    def __eq__(self, other:object) -> bool:
        if  super().__eq__(other) == True and self.__conductivite == other.__conductivite and self.__valeur == other.__valeur:
            return True
        
        return False

    def __hash__(self):
        qualite_mineraux = super().__hash__()
        return hash((qualite_mineraux, self.__conductivite, self.__valeur))

    def est_precieux(self) -> bool:
        if self.__valeur > 50:
            return True
        
        return False
   
    def score(self):
        return super().score() + self.__valeur * 5
    
    def liste_metaux(mineraux:list) -> str:

        '''
        Cette fonction permet d'afficher tous les nom et numéro des minéraux
        Elle reçoit la liste des minéraux
        Elle retourne le texte affichant le nom et le numéro des minéraux
        '''

        text = ""
        for x in mineraux:
            if type(x) is Metal:
                text += f"\nMinéral №{x.get_numero()}: {x.get_nom()}"
       
        return text
    