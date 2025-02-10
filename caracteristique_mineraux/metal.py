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
        return self.afficher()
    
    def __eq__(self, other:object) -> bool:
        return self.__nom == other.__nom and self.__formule_chimique == other.__formule_chimique and self.__couleur == other.__couleur and self.__lustre == other.__lustre and self.__radioactivite == other.__radioactivite and self.__durete == other.__durete and self.__masse_volumique == other.__masse_volumique and self.__conductivite == other.__conductivite and self.__valeur == other.__valeur

    def __hash__(self):
        return 

    def est_precieux(self) -> bool:
        if self.__valeur > 50:
            return True
        
        return False
    
    def afficher(self) -> str:
        text = f"==================== Minéral №{self.get_numero()} ==================== \nNom: {self.get_nom()} \nFormule Chimique: {self.get_formule_chimique()}\nCouleur: ({self.get_couleur().description()}) \nDensité: {self.get_masse_volumique()}g/cm3 \nDureté: {self.get_durete()} ({self.classement_durete()}) \nConductivité: {self.get_conductivite()}S/m \nValeur: {self.get_valeur()}$/kg"

        if self.get_radioactivite() == True:
            text += "\n========== DANGER! ÉLÉMENT RADIOACTIF =========="

        return text
