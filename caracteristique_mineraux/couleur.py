class CouleurRGB:

    '''Cette classe décrit une couleur selon ses valeurs RGB'''

    def __init__(self, r:int, g:int, b:int):
       
        '''
        Fonction qui sert à construire de nouveux objets de classe Couleur.
        Il assigne les attributs: r(ed), g(reen), et b(lue) aux objets qui sont stockés dans la base de données
        '''

        self.__r = r
        self.__g = g
        self.__b = b

    def get_r(self):

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut r(ed) d'un objet CouleurRGB
        Il retourne la valeur R la couleurRGB
        '''

        return self.__r
   
    def get_g(self):

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut g(reen) d'un objet CouleurRGB
        Il retourne la valeur G la couleurRGB
        '''

        return self.__g
   
    def get_b(self):

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut b(lue) d'un objet CouleurRGB
        Il retourne la valeur B la couleurRGB
        '''

        return self.__b

    def description(self) -> str:

        '''
        Cette fonction permet d'afficher la description d'une couleur (ses valeurs RGB)
        Elle retourne les trois valeurs RGB de la couleur sous forme de texte
        '''

        return f"{self.__r}, {self.__g}, {self.__b}"
   