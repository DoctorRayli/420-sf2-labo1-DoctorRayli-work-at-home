from caracteristique_mineraux.mineral import Mineral
from caracteristique_mineraux.couleur import CouleurRGB

class Gemme(Mineral):

    '''Cette classe décrit un gemme selon son numéro, nom, formule chimique, couleur, lustre, radioactivité, dureté,la masse volumique et clarté'''

    def __init__(self, numero:int, nom:str, formule_chimique:str,  couleur:CouleurRGB, lustre:str, radioactivite:bool, durete:int, masse_volumique:float, clarte:str):
        
        '''
        Fonction qui sert à construire de nouveux objets de classe Gemme.
        Il assigne les attributs: numéro, nom, formule chimique, couleur, lustre, radioactivité, dureté, masse volumique et clarté aux objets qui sont stockés dans la base de données
        '''

        super().__init__(numero, nom, formule_chimique,  couleur, lustre, radioactivite, durete, masse_volumique)
        self.__clarte = clarte  

    def __str__(self) -> str:

        '''
        Cette fonction redéfini la méthode spéciale 'str' qui permet maintenant d'afficher les détails d'un minéral: numero, nom, formule chimique, couleur, masse volumique, dureté et clarté
        Elle retourne les attributs d'un gemme sous forme de texte
        '''

        text = super().__str__()
        text += f"\nClarté: {self.get_clarte()} ({self.classement_clarte()}) \nScore: {self.score():.3f}"
        if self.get_radioactivite() == True:
            text += "\n========== DANGER! ÉLÉMENT RADIOACTIF =========="

        return text
    
    def __eq__(self, other:object) -> bool:

        '''
        Cette fonction redéfini la méthode spéciale '=='
        Elle retourne une valeur booléenne confirmant l'égalité ou non de deux objet de type Gemme
        '''

        if  super().__eq__(other) == True and self.__clarte == other.__clarte:
            return True
        
        return False 
    
    def __hash__(self) -> int:

        '''
        Cette fonction redéfini la méthode spéciale 'hash()'
        Elle retourne un hash déterminé par les attributs d'un object de type Gemme
        '''

        qualite_mineraux = super().__hash__()
        return hash((qualite_mineraux, self.__clarte))

    def get_clarte(self) -> str:

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut clarté d'un objet Gemme
        Il retourne la clarté du gemme
        '''

        return self.__clarte
    
    def classement_clarte(self) -> str:

        '''
        Cette fonction permet de convertir l'index de clarté en mots
        Elle retourne le texte contenant la classification en mots
        '''

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

    def est_precieux(self) -> bool:

        '''
        Cette fonction détermine si une gemme est précieuse
        Elle retourne que oui, une gemme est précieuse
        '''

        return True
    
    def score(self) -> float:

        '''
        Cette fonction permet de calculer le score(puissance) d'une gemme
        Elle retourne le score de la gemme
        '''

        point_mineral = 0
        match self.__clarte:
            case "IF":
                point_mineral = 1000

            case "VVS":
                point_mineral = 700

            case "VS":
                point_mineral = 500

            case "SI":
                point_mineral = 200

        return super().score() + point_mineral
    
    def liste_gemmes(mineraux:list) -> str:

        '''
        Cette fonction permet d'afficher tous les nom et numéro des gemmes
        Elle reçoit la liste des minéraux
        Elle retourne le texte affichant le nom et le numéro des gemmes
        '''

        text = ""
        for x in mineraux:
            if type(x) is Gemme:
                text += f"\nMinéral №{x.get_numero()}: {x.get_nom()}"
       
        return text
