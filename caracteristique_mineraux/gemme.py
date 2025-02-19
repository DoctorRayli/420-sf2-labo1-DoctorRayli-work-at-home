from caracteristique_mineraux.mineral import Mineral
from caracteristique_mineraux.couleur import CouleurRGB

'''Addon sur le laboratoire 1'''

class Gemme(Mineral):

    ''''''

    def __init__(self, numero:int, nom:str, formule_chimique:str,  couleur:CouleurRGB, lustre:str, radioactivite:bool, durete:int, masse_volumique:float, clarte:str):
        super().__init__(numero, nom, formule_chimique,  couleur, lustre, radioactivite, durete, masse_volumique)
        self.__clarte = clarte  

    def get_clarte(self):
        return self.__clarte
    
    def __str__(self) -> str:
        text = super().__str__()
        text += f"\nClarté: {self.get_clarte()} ({self.classement_clarte()}) \nScore: {self.score():.3f}"
        if self.get_radioactivite() == True:
            text += "\n========== DANGER! ÉLÉMENT RADIOACTIF =========="

        return text
    
    def __hash__(self):
        qualite_mineraux = super().__hash__()
        return hash((qualite_mineraux, self.__clarte))
    
    def classement_clarte(self):
        if self.__clarte == "IF":
            return "Internally Flawless"
        
        elif self.__clarte == "VCS":
            return "Very Very Slightly Included"
        
        elif self.__clarte == "VS":
            return "Very Slightly Included"
        
        elif self.__clarte == "SI":
            return "Slightly Included"
        
        elif self.__clarte == "I":
            return "Included"

    def est_precieux(self) -> bool:
        return True
    
    def score(self):
        point_mineral = 0
        match self.__clarte:
            case "IF":
                point_mineral = 100

            case "VVS":
                point_mineral = 70

            case "VS":
                point_mineral = 50

            case "SI":
                point_mineral = 20

        return super().score() + point_mineral
    
    def liste_gemme(mineraux:list) -> str:

        '''
        Cette fonction permet d'afficher tous les nom et numéro des minéraux
        Elle reçoit la liste des minéraux
        Elle retourne le texte affichant le nom et le numéro des minéraux
        '''

        text = ""
        for x in mineraux:
            if type(x) is Gemme:
                text += f"\nMinéral №{x.get_numero()}: {x.get_nom()}"
       
        return text
