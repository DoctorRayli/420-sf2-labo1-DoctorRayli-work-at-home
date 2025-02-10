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
        return self.afficher()
    
    def classement_clarte(self):
        if self.__clarte == "IF":
            return "Internally Flawless"
        
        elif self.__clarte == "VVS":
            return "Very Very Slightly Included"
        
        elif self.__clarte == "VS":
            return "Very Slightly Included"
        
        elif self.__clarte == "SI":
            return "Slightly Included"
        
        elif self.__clarte == "I":
            return "Included"

    def afficher(self) -> str:
        text = f"==================== Minéral №{self.get_numero()} ==================== \nNom: {self.get_nom()} \nFormule Chimique: {self.get_formule_chimique()}\nCouleur: ({self.get_couleur.description()}) \nDensité: {self.get_masse_volumique()}g/cm3 \nDureté: {self.get_durete()} ({self.classement_durete()}) \nClarté: {self.get_clarte()} ({self.classement_clarte()})"

        if self.get_radioactivite() == True:
            text += "\n========== DANGER! ÉLÉMENT RADIOACTIF =========="

        return text

    def est_precieux(self) -> bool:
        return True
