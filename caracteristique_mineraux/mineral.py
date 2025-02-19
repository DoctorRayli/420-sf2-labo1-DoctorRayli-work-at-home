from caracteristique_mineraux.couleur import CouleurRGB

class Mineral:

    '''Cette classe décrit un minéral selon son numéro, nom, formule chimique, couleur, lustre, radioactivité, dureté et la masse volumique'''

    nb_combat = 0
   
    def __init__(self, numero:int, nom:str, formule_chimique:str,  couleur:CouleurRGB, lustre:str, radioactivite:bool, durete:int, masse_volumique:float):

        '''
        Fonction qui sert à construire de nouveux objets de classe Mineral.
        Il assigne les attributs: numéro, nom, formule chimique, couleur, lustre, radioactivité, dureté et masse volumique aux objets qui sont stockés dans la base de données
        '''

        self.__numero = numero
        self.__nom = nom
        self.__formule_chimique = formule_chimique
        self.__couleur = couleur
        self.__lustre = lustre
        self.__radioactivite = radioactivite
        self.__durete = durete
        self.__masse_volumique = masse_volumique

    def __str__(self) -> str:
        
        '''
        Cette fonction permet d'afficher les détails d'un minéral: numero, nom, formule chimique, couleur, masse volumique, dureté
        Elle retourne les attributs d'un minéral sous forme de texte
        '''

        text = f"==================== Minéral №{self.__numero} ==================== \nNom: {self.__nom} \nFormule Chimique: {self.__formule_chimique}\nCouleur: ({str(self.__couleur)}) \nDensité: {self.__masse_volumique}g/cm3 \nDureté: {self.__durete} ({self.classement_durete()})"

        if self.__radioactivite == True and type(self) is Mineral:
            text += "\n========== DANGER! ÉLÉMENT RADIOACTIF =========="

        return text
    
    def __eq__(self:object, other:object) -> bool:
        if self.__nom == other.__nom and self.__formule_chimique == other.__formule_chimique and self.__couleur == other.__couleur and self.__lustre == other.__lustre and self.__radioactivite == other.__radioactivite and self.__durete == other.__durete and self.__masse_volumique == other.__masse_volumique:
            return True
        
        return False 
    
    def __hash__(self):
        return hash((self.__numero, self.__nom, self.__formule_chimique, self.__couleur, self.__lustre, self.__radioactivite, self.__durete, self.__masse_volumique))

    def get_numero(self):

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut numero d'un objet Mineral
        Il retourne le numéro du minéral
        '''

        return self.__numero
   
    def get_nom(self):

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut nom d'un objet Mineral
        Il retourne le nom du minéral
        '''
         
        return self.__nom

    def get_formule_chimique(self):

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut formule chimique d'un objet Mineral
        Il retourne la formule chimique du minéral
        '''

        return self.__formule_chimique
   
    def get_couleur(self):

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut couleur d'un objet Mineral
        Il retourne la couleur du minéral
        '''

        return self.__couleur
   
    def get_lustre(self):

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut lustre d'un objet Mineral
        Il retourne le lustre du minéral
        '''

        return self.__lustre
   
    def get_radioactivite(self):

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut radioactivité d'un objet Mineral
        Il retourne le radioactivité du minéral
        '''

        return self.__radioactivite
   
    def get_durete(self):

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut dureté d'un objet Mineral
        Il retourne le dureté du minéral
        '''

        return self.__durete
   
    def get_masse_volumique(self):

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut masse volumique d'un objet Mineral
        Il retourne le masse volumique du minéral
        '''

        return self.__masse_volumique

    def classement_durete(self) -> str:

        '''
        Cette fonction permet de convertir l'index de dureté en une catégorie (très mou, mou, moyen, dur et très dur)
        Elle retourne le texte décrivant la catégorie du minéral
        '''

        if self.__durete < 2:
            return "très mou"
       
        elif self.__durete < 5:
            return "mou"

        elif self.__durete < 7:
            return "moyen"

        elif self.__durete < 10:
            return "dur"

        else:
            return "très dur"

    def liste_mineraux(mineraux:list) -> str:

        '''
        Cette fonction permet d'afficher tous les nom et numéro des minéraux
        Elle reçoit la liste des minéraux
        Elle retourne le texte affichant le nom et le numéro des minéraux
        '''

        text = ""
        for x in mineraux:
            text += f"\nMinéral №{x.__numero}: {x.__nom}"
       
        return text

    def masse_a_volume(self, masse) -> float:

        '''
        Cette fonction calcul le volume d'un minéral à partir de leur masse
        Elle retourne le volume
        '''

        return masse / self.__masse_volumique
   
    def volume_a_masse(self, volume) -> float:

        '''
        Cette fonction calcul la masse d'un minéral à partir de leur volume
        Elle retourne la masse
        '''

        return volume * self.__masse_volumique
   
    def est_precieux(self) -> bool:
        return False
    
    def score(self):
        
        point_mineral = 0

        point_mineral += self.__durete * 10 + self.__masse_volumique

        if self.__radioactivite == True:
            point_mineral += 1000

        return point_mineral
    
    def combat_de_mineraux(mineral_numero_1:object, mineral_numero_2:object):

        '''
        Cette fonction détermine le gagnant, le perdant et du pointage d'un combat de 2 minéraux
        Elle reçoit les deux minéraux
        Elle retourne le gagnant, le perdant, le type de victoire et un texte affichant les données mentionnées précédemment
        '''

        Mineral.nb_combat += 1

        if mineral_numero_1.score() > mineral_numero_2.score():
            return mineral_numero_1, mineral_numero_2, mineral_numero_1.score(), mineral_numero_2.score(), f"\n==========Combat №{Mineral.nb_combat}==========\nLe {mineral_numero_1.get_nom()} ({mineral_numero_1.get_numero()}) a battu le {mineral_numero_2.get_nom()} ({mineral_numero_2.get_numero()}) de {mineral_numero_1.score() - mineral_numero_2.score():.3f} points"

        elif mineral_numero_2.score() > mineral_numero_1.score():
            return mineral_numero_2, mineral_numero_1, mineral_numero_2.score(), mineral_numero_1.score(), f"\n==========Combat №{Mineral.nb_combat}==========\nLe {mineral_numero_2.get_nom()} ({mineral_numero_2.get_numero()}) a battu le {mineral_numero_1.get_nom()} ({mineral_numero_1.get_numero()}) de {mineral_numero_2.score() - mineral_numero_1.score():.3f} points"

        else:
            return mineral_numero_1, mineral_numero_2, mineral_numero_1.score(), mineral_numero_1.score(), f"\n==========Combat №{Mineral.nb_combat}==========\nLe {mineral_numero_1.get_nom()} ({mineral_numero_1.get_numero()}) a une force égale au {mineral_numero_2.get_nom()} ({mineral_numero_2.get_numero()}) à {mineral_numero_1.score():.3f} points"
