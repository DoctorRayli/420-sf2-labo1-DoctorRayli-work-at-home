from caracteristique_mineraux.mineral import Mineral
from caracteristique_mineraux.couleur import CouleurRGB

class Metal(Mineral):

    '''Cette classe décrit un métal selon son numéro, nom, formule chimique, couleur, lustre, radioactivité, dureté, masse volumique, valeur et conductivité'''

    def __init__(self, numero:int, nom:str, formule_chimique:str,  couleur:CouleurRGB, lustre:str, radioactivite:bool, durete:int, masse_volumique:float, conductivite:float, valeur:float):
        
        '''
        Fonction qui sert à construire de nouveux objets de classe Métal.
        Il assigne les attributs: numéro, nom, formule chimique, couleur, lustre, radioactivité, dureté, masse volumique, valeur et conductivité aux objets qui sont stockés dans la base de données
        '''
        
        super().__init__(numero, nom, formule_chimique,  couleur, lustre, radioactivite, durete, masse_volumique)
        self.__conductivite = conductivite
        self.__valeur = valeur

    def __str__(self) -> str:

        '''
        Cette fonction redéfini la méthode spéciale 'str' qui permet maintenant d'afficher les détails d'un minéral: numero, nom, formule chimique, couleur, masse volumique, dureté, valeur et conductivité
        Elle retourne les attributs d'un métal sous forme de texte
        '''

        text = super().__str__() 
        text += f"\nConductivité: {self.__conductivite}S/m \nValeur: {self.__valeur}$/kg \nScore: {self.score():.3f}"
        if self.get_radioactivite() == True:
            text += "\n========== DANGER! ÉLÉMENT RADIOACTIF =========="

        return text
    
    def __eq__(self, other:object) -> bool:

        '''
        Cette fonction redéfini la méthode spéciale '=='
        Elle retourne une valeur booléenne confirmant l'égalité ou non de deux objet de type Métal
        '''

        if  super().__eq__(other) == True and self.__conductivite == other.__conductivite and self.__valeur == other.__valeur:
            return True
        
        return False

    def __hash__(self) -> int:

        '''
        Cette fonction redéfini la méthode spéciale 'hash()'
        Elle retourne un hash déterminé par les attributs d'un object de type Métal
        '''

        qualite_mineraux = super().__hash__()
        return hash((qualite_mineraux, self.__conductivite, self.__valeur))    

    def get_conductivite(self) -> float:

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut conductivité d'un objet Métal
        Il retourne le conductivité du métal
        '''

        return self.__conductivite
    
    def get_valeur(self) -> float:

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut valeur d'un objet Métal
        Il retourne la valeur du métal
        '''

        return self.__valeur

    def est_precieux(self) -> bool:

        '''
        Cette fonction détermine si un métal est précieuse
        Elle retourne une valeur booléenne qui confirme ou non si un métal est précieux
        '''

        if self.__valeur > 50:
            return True
        
        return False
   
    def score(self) -> float:

        '''
        Cette fonction permet de calculer le score(puissance) d'un métal
        Elle retourne le score du métal
        '''

        return super().score() + self.__valeur * 5
    
    def liste_metaux(mineraux:list) -> str:

        '''
        Cette fonction permet d'afficher tous les nom et numéro des métaux
        Elle reçoit la liste des minéraux
        Elle retourne le texte affichant le nom et le numéro des métaux
        '''

        text = ""
        for x in mineraux:
            if type(x) is Metal:
                text += f"\nMinéral №{x.get_numero()}: {x.get_nom()}"
       
        return text
    