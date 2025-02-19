from caracteristique_mineraux.metal import Metal
from caracteristique_mineraux.couleur import CouleurRGB

class Alliage:
    def __init__(self, numero:int, nom:str, metaux:dict):
        
        self.__numero = numero
        self.__nom = nom
        self.__metaux = metaux
        self.__masse_volumique = Alliage.calcul_masse_volumique(metaux)
        self.__couleur = Alliage.calcul_couleur(metaux)
        self.__radioactivite = Alliage.est_radioactif(metaux)
        self.__durete = Alliage.calcul_durete(metaux)
        self.__valeur = Alliage.calcul_valeur(metaux)
        self.__conductivite = Alliage.calcul_conductivite(metaux)

    def __str__(self):
        
        '''
        Fonction qui retourne une description détaillée d'un alliage au choix (nom, masse volumique, couleur, radioactivité, dureté, conductivité et liste de métaux)
        Il averti l'utilisateur si l'alliage contient un métal radioactif
        Il retourne un texte (la description détaillée)
        '''

        nb_element_radioactif = 0

        text = f"==================== Alliage №{self.__numero} ==================== \nNom: {self.__nom} \nCouleur: ({str(self.__couleur)}) \nDensité: {self.__masse_volumique}g/cm3 \nDureté: {self.__durete} ({self.classement_durete()}) \nMétaux: "

        for x in self.__metaux:
            text += f"Métal № {x.get_numero()}: {x.get_nom()} ({Alliage.proportion_metal(self.__metaux[x], self.__metaux) * 100:.3f}%), "

        for x in self.__metaux:
            if x.get_radioactivite() == True:
                nb_element_radioactif += 1
               
        if nb_element_radioactif > 0:
            text += f"\n========== DANGER! PRÉSENCE DE {nb_element_radioactif} ÉLÉMENTS RADIOACTIFS =========="

        return text

    def get_numero(self) -> str:
        return self.__numero

    def get_nom(self) -> str:
        return self.__nom
    
    def get_metaux(self):
        return self.__metaux
    
    def get_masse_volumique(self) -> str:
        return self.__masse_volumique
    
    def get_couleur(self) -> str:
        return self.__couleur
    
    def get_radioactivite(self) -> str:
        return self.__radioactivite
    
    def get_durete(self) -> str:
        return self.__durete
    
    def get_conductivite(self) -> str:
        return self.__conductivite

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
    
    def masse_total(metaux:dict):
        masse_total = 0
        
        for x in metaux:
            masse_total += metaux[x]

        return masse_total
    
    def proportion_metal(masse_metal, metaux:dict):
        return masse_metal/Alliage.masse_total(metaux)

    def calcul_masse_volumique(metaux:dict):
        masse_volumique = 0

        for x in metaux:
            masse_volumique += x.get_masse_volumique() * Alliage.proportion_metal(metaux[x], metaux)

        return masse_volumique
    
    def calcul_couleur(metaux:dict):
        r = 0
        g = 0
        b = 0

        for x in metaux:
            r += x.get_couleur().get_r() * Alliage.proportion_metal(metaux[x], metaux)

        for x in metaux:
            g += x.get_couleur().get_g() * Alliage.proportion_metal(metaux[x], metaux)

        for x in metaux:
            b += x.get_couleur().get_b() * Alliage.proportion_metal(metaux[x], metaux)
        
        return CouleurRGB(r, g, b)

    def est_radioactif(metaux:dict):
        for x in metaux:
            if x.get_radioactivite() == True:
                return True
        
        return False
    
    def calcul_durete(metaux:dict):
        durete = 0

        for x in metaux:
            durete += x.get_durete() * Alliage.proportion_metal(metaux[x], metaux)

        return durete
    
    def calcul_conductivite(metaux:dict):
        conductivite = 0

        for x in metaux:
            conductivite += x.get_conductivite() * Alliage.proportion_metal(metaux[x], metaux)

        return conductivite
    
    def calcul_valeur(metaux:dict):
        valeur = 0

        for x in metaux:
            valeur += x.get_valeur() *Alliage.proportion_metal(metaux[x], metaux)

        return valeur
    
    def liste_alliages(alliages:list) -> str:

        '''
        Cette fonction permet d'afficher tous les nom et numéro des alliages
        Elle reçoit la liste des alliages
        Elle retourne le texte affichant le nom et le numéro des minéraux
        '''

        text = ""
        for x in alliages:
            text += f"\nAlliage №{x.__numero}: {x.__nom}"
       
        return text
    
    def afficher_metaux(self):
        liste_metaux = ""
        for x in self.__metaux:
            liste_metaux += f"\n{x.get_nom()}: numéro {x.get_numero()}"

        return f"\nParmi les métaux: {liste_metaux}"
    
    def ajout_metal(self, metal:Metal, masse:float):
        
        for x in self.__metaux:
            if x == metal:
                self.__metaux[x] += masse

                return f"{masse}g de {x.get_nom()} a été ajouté dans le {self.__nom}, donc il y en a maintenant {self.__metaux[x]}g dans l'alliage"
            
        self.__metaux[metal] = masse

        return f"{masse}g de {metal.get_nom()} a été ajouté dans le {self.__nom}"

    def est_present_dans_alliage(self, metal):
        for x in self.__metaux:
            if x == metal:
                return True
        
        return False
    
    def soustrait_metal(self, metal:Metal, masse:float):
        for x in self.__metaux:
            if x == metal:
                self.__metaux[x] -= masse

                if self.__metaux[x] == 0:
                    self.__metaux.pop(x)
                    return f"{masse}g de {x.get_nom()} a été enlevé dans le {self.__nom}, donc il y en a maintenant 0g dans l'alliage"

                return f"{masse}g de {x.get_nom()} a été enlevé dans le {self.__nom}, donc il y en a maintenant {self.__metaux[x]}g dans l'alliage"
            
    def score(self):
        
        point_alliage = 0
        point_alliage += self.__durete * 10 + self.__masse_volumique

        if self.__radioactivite == True:
            point_alliage += 1000

        point_alliage += self.__valeur * 5

        return point_alliage

    def combat_alliages_metaux(combatant_1, combatant_2):
        pass