from caracteristique_mineraux.metal import Metal
from caracteristique_mineraux.mineral import Mineral
from caracteristique_mineraux.couleur import CouleurRGB

class Alliage:

    '''Cette classe décrit un alliage selon son numéro, nom, dictionnaire de métaux et leur masse, couleur, lustre, radioactivité, dureté, masse volumique, valeur et conductivite'''

    def __init__(self, numero:int, nom:str, metaux:dict):
        
        '''
        Fonction qui sert à construire de nouveux objets de classe Alliage.
        Il assigne les attributs: numéro, nom, dictionnaire de métaux et leur masse, couleur, lustre, radioactivité, dureté, masse volumique, valeur et conductivite aux objets qui sont stockés dans la base de données
        '''
        self.__numero = numero
        self.__nom = nom
        self.__metaux = metaux
        self.__masse_volumique = Alliage.calcul_masse_volumique(metaux)
        self.__couleur = Alliage.calcul_couleur(metaux)
        self.__lustre = "Métallique"
        self.__radioactivite = Alliage.est_radioactif(metaux)
        self.__durete = Alliage.calcul_durete(metaux)
        self.__valeur = Alliage.calcul_valeur(metaux)
        self.__conductivite = Alliage.calcul_conductivite(metaux)

    def __str__(self) -> str:
        
        '''
        Fonction qui redéfini la méthode spéciale 'str' qui permet maintenant de retourner une description détaillée d'un alliage au choix (nom, masse volumique, couleur, lustre, radioactivité, dureté, valeur, conductivité et liste de métaux)
        Il averti l'utilisateur si l'alliage contient un métal radioactif
        Il retourne un texte (la description détaillée)
        '''

        nb_element_radioactif = 0

        text = f"==================== Alliage №{self.__numero} ==================== \nNom: {self.__nom} \nCouleur: ({str(self.__couleur)}) \nDensité: {self.__masse_volumique:.3f}g/cm3 \nDureté: {self.__durete:.3f} ({self.classement_durete()}) \nConductivité: ({self.__conductivite[0]} à {self.__conductivite[1]}) S/m \nValeur: {self.__valeur}$/kg \nScore: {self.score():.3f} \nMétaux: "
        for x in self.__metaux:
            text += f"Métal № {x.get_numero()}: {x.get_nom()} ({Alliage.proportion_metal(self.__metaux[x], self.__metaux) * 100:.3f}%), "

        for x in self.__metaux:
            if x.get_radioactivite() == True:
                nb_element_radioactif += 1
               
        if nb_element_radioactif > 0:
            text += f"\n========== DANGER! PRÉSENCE DE {nb_element_radioactif} ÉLÉMENTS RADIOACTIFS =========="

        return text

    def get_numero(self) -> int:

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut numero d'un objet Alliage
        Il retourne le numéro de l'alliage
        '''
           
        return self.__numero

    def get_nom(self) -> str:

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut nom d'un objet Alliage
        Il retourne le nom de l'alliage
        '''

        return self.__nom
    
    def get_metaux(self) -> dict[Metal, float]:

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut métaux d'un objet Alliage
        Il retourne le dictionnaire de métaux et leur masse de l'alliage
        '''

        return self.__metaux
    
    def get_masse_volumique(self) -> float:

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut masse volumique d'un objet Alliage
        Il retourne la masse volumique de l'alliage
        '''

        return self.__masse_volumique
    
    def get_couleur(self) -> CouleurRGB:

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut couleur RGB d'un objet Alliage
        Il retourne la couleur RGB de l'alliage
        '''

        return self.__couleur
    
    def get_lustre(self) -> str:

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut lustre d'un objet Alliage
        Il retourne le lustre de l'alliage
        '''

        return self.__lustre
    
    def get_radioactivite(self) -> bool:

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut radioactivité d'un objet Alliage
        Il retourne la radioactivité de l'alliage
        '''

        return self.__radioactivite
    
    def get_durete(self) -> float:

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut dureté d'un objet Alliage
        Il retourne la dureté de l'alliage
        '''

        return self.__durete
    
    def get_valeur(self) -> float:

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut valeur d'un objet Alliage
        Il retourne la valeur de l'alliage
        '''

        return self.__valeur
    
    def get_conductivite(self) -> list[float]:

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut conductivité d'un objet Alliage
        Il retourne la valeur de l'alliage
        '''

        return self.__conductivite

    def classement_durete(self) -> str:

        '''
        Cette fonction permet de convertir l'index de dureté en une catégorie (très mou, mou, moyen, dur et très dur)
        Elle retourne le texte décrivant la catégorie de l'alliage
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
        
    def calcul_masse_volumique(metaux:dict[Metal, float]) -> float:

        '''
        Cette fonction permet de calculer la masse volumique d'un alliage
        Elle reçoit le dictionnaire de métaux-masse
        Elle retourne la masse volumique de l'alliage
        '''

        masse_volumique = 0

        for x in metaux:
            masse_volumique += x.get_masse_volumique() * Alliage.proportion_metal(metaux[x], metaux)

        return masse_volumique
    
    def calcul_couleur(metaux:dict[Metal, float]) -> CouleurRGB:

        '''
        Cette fonction permet de calculer la couleur RGB d'un alliage
        Elle reçoit le dictionnaire de métaux-masse
        Elle retourne la couleur RGB de l'alliage
        '''

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

    def est_radioactif(metaux:dict[Metal, float]) -> bool:

        '''
        Cette fonction permet de vérifier la radioactivité d'un alliage
        Elle reçoit le dictionnaire de métaux-masse
        Elle retourne la radioactivité de l'alliage
        '''

        for x in metaux:
            if x.get_radioactivite() == True:
                return True
        
        return False
    
    def calcul_durete(metaux:dict[Metal, float]) -> float:

        '''
        Cette fonction permet de calculer la dureté d'un alliage
        Elle reçoit le dictionnaire de métaux-masse
        Elle retourne la dureté de l'alliage
        '''

        durete = 0

        for x in metaux:
            durete += x.get_durete() * Alliage.proportion_metal(metaux[x], metaux)

        return durete
    
    def calcul_conductivite(metaux:dict[Metal, float]) -> list[float]:

        '''
        Cette fonction permet de calculer l'intervalle de conductivité d'un alliage
        Elle reçoit le dictionnaire de métaux-masse
        Elle retourne l'intervalle de conductivité de l'alliage
        '''

        borne_inferieur = 0
        borne_superieur = 0

        for x in metaux:
            borne_inferieur += Alliage.proportion_metal(metaux[x], metaux) / x.get_conductivite()
            borne_superieur += Alliage.proportion_metal(metaux[x], metaux) * x.get_conductivite()
        
        conductivite = [1 / borne_inferieur, borne_superieur]
        return conductivite
        
    def calcul_valeur(metaux:dict[Metal, float]) -> float:

        '''
        Cette fonction permet de calculer la valeur d'un alliage
        Elle reçoit le dictionnaire de métaux-masse
        Elle retourne la valeur de l'alliage
        '''

        valeur = 0

        for x in metaux:
            valeur += x.get_valeur() *Alliage.proportion_metal(metaux[x], metaux)

        return valeur
    
    def masse_total(metaux:dict[Metal, float]) -> float:

        '''
        Cette fonction permet de calculer la masse totale d'un alliage
        Elle reçoit le dictionnaire de métaux-masse
        Elle retourne la masse totale de l'alliage
        '''

        masse_total = 0
        
        for x in metaux:
            masse_total += metaux[x]

        return masse_total
    
    def proportion_metal(masse_metal:float, metaux:dict[Metal, float]) -> float:

        '''
        Cette fonction permet de calculer la proportion d'un métal dans d'un alliage
        Elle reçoit le dictionnaire de métaux-masse et la masse totale
        Elle retourne la proportion d'un métal de l'alliage
        '''

        return masse_metal/Alliage.masse_total(metaux)
    
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
    
    def afficher_metaux(self) -> str:

        '''
        Cette fonction permet d'afficher tous les nom et numéro des métaux dans un alliage
        Elle retourne le texte affichant le nom et le numéro des métaux dans l'alliage
        '''

        liste_metaux = ""
        for x in self.__metaux:
            liste_metaux += f"\n{x.get_nom()}: numéro {x.get_numero()}"

        return f"\nParmi les métaux: {liste_metaux}"
    
    def ajout_metal(self, metal:Metal, masse:float) -> str:

        '''
        Cette fonction permet d'ajouter des grammes de métaux dans un alliage
        Elle reçoit le métal ajouté et la masse ajouté
        Elle retourne un texte affirmant l'ajout
        '''
        
        for x in self.__metaux:
            if x == metal:
                self.__metaux[x] += masse

                return f"{masse}g de {x.get_nom()} a été ajouté dans le {self.__nom}, donc il y en a maintenant {self.__metaux[x]}g dans l'alliage"
            
        self.__metaux[metal] = masse

        return f"{masse}g de {metal.get_nom()} a été ajouté dans le {self.__nom}"

    def est_present_dans_alliage(self, metal:Metal) -> bool:

        '''
        Cette fonction permet de vérifier qu'un métal qu'on veut retirer d'un alliage est présent dans l'alliage
        Elle reçoit le métal qu'on veut retirer
        Elle retourne une valeur booléenne qui affirme la présence ou non du métal dans l'alliage
        '''

        for x in self.__metaux:
            if x == metal:
                return True
        
        return False
    
    def soustrait_metal(self, metal:Metal, masse:float) -> str:

        '''
        Cette fonction permet de soustraire une masse d'un métal présent dans un alliage
        Elle reçoit le métal qu'on veut retirer et la masse qu'on veut retirer
        Elle retourne un texte affirmant que le métal a été soustrait de l'alliage
        '''

        for x in self.__metaux:
            if x == metal:
                self.__metaux[x] -= masse

                if self.__metaux[x] == 0:
                    self.__metaux.pop(x)
                    return f"{masse}g de {x.get_nom()} a été enlevé dans le {self.__nom}, donc il y en a maintenant 0g dans l'alliage"

                return f"{masse}g de {x.get_nom()} a été enlevé dans le {self.__nom}, donc il y en a maintenant {self.__metaux[x]}g dans l'alliage"
            
    def score(self) -> float:

        '''
        Cette fonction permet de calculer le score(puissance) d'un alliage
        Elle retourne le score de l'alliage
        '''
        
        point_alliage = 0
        point_alliage += self.__durete * 10 + self.__masse_volumique

        if self.__radioactivite == True:
            point_alliage += 1000

        point_alliage += self.__valeur * 5

        return point_alliage
    
    def creation(alliages:list, nom:str, metaux_alliage:dict[Metal, float]) -> list:

        '''
        Fonction permettant à l'utilisateur de créer son propre allaige en appelant la fonction __init__
        Il l'ajoute à la liste de collection existante

        Il reçoit tous les données nécéssaire pour la création d'un alliage (nom et dictionnaire de métaux-masse)
        Il retourne la liste d'alliages modifiée
        '''

        alliages.append(Alliage(len(alliages) + 1, nom, metaux_alliage))
        return alliages
