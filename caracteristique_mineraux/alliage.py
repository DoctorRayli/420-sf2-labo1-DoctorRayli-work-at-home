from caracteristique_mineraux.metal import Metal

class Alliage:
    def __init__(self, nom:str, metaux:dict):
        

        self.__nom = nom
        self.__liste_metaux = metaux
        self.__masse_volumique = Alliage.calcul_masse_volumique(metaux)

    def calcul_masse_volumique(metaux:dict):
        masse_volumique = 0
        masse_totale = 0

        for x in metaux.values():
            masse_totale += x

        for x in metaux:
            masse_volumique += x.get_masse_volumique() * metaux[x]/masse_totale

        return masse_volumique
