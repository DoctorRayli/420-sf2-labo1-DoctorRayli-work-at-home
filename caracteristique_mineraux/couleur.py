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

    def __str__(self) -> str:

        '''
        Cette fonction permet d'afficher les détails d'une couleur RGB: r, g et b
        Elle retourne les attributs d'une couleur sous forme de texte
        '''

        return f"{self.__r:.3f}, {self.__g:.3f}, {self.__b:.3f}"

    def __eq__(self, other:object) -> bool:

        '''
        Cette fonction redéfini la méthode spéciale '=='
        Elle retourne une valeur booléenne confirmant l'égalité ou non de deux objet de type CouleurRGB
        '''

        if self.__r == other.__r and self.__g == other.__g and self.__b == other.__b:
            return True
        
        return False

    def __hash__(self) -> int:

        '''
        Cette fonction redéfini la méthode spéciale 'hash()'
        Elle retourne un hash déterminé par les attributs d'un object de type Couleur RGB
        '''

        return hash((self.__r, self.__g, self.__b))

    def get_r(self) -> int:

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut r(ed) d'un objet CouleurRGB
        Il retourne la valeur R la couleurRGB
        '''

        return self.__r
   
    def get_g(self) -> int:

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut g(reen) d'un objet CouleurRGB
        Il retourne la valeur G la couleurRGB
        '''

        return self.__g
   
    def get_b(self) -> int:

        '''
        Fonction d'encapsulation qui sert à permettre l'accès à l'attribut b(lue) d'un objet CouleurRGB
        Il retourne la valeur B la couleurRGB
        '''

        return self.__b
   