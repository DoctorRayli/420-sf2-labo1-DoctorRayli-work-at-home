from caracteristique_mineraux.mineral import Mineral
from caracteristique_mineraux.gemme import Gemme
from caracteristique_mineraux.metal import Metal


def combat_de_mineraux(mineral_numero_1:object, mineral_numero_2:object):

        '''
        Cette fonction détermine le gagnant, le perdant et du pointage d'un combat de 2 minéraux
        Elle reçoit les deux minéraux
        Elle retourne le gagnant, le perdant, le type de victoire et un texte affichant les données mentionnées précédemment
        '''

        Mineral.nb_combat += 1

        point_mineral_1 = 0
        point_mineral_2 = 0

        point_mineral_1 += mineral_numero_1.get_durete() * 10 + mineral_numero_1.get_masse_volumique()
        point_mineral_2 += mineral_numero_2.get_durete() * 10 + mineral_numero_2.get_masse_volumique()

        if mineral_numero_1.get_radioactivite() == True:
            point_mineral_1 += 1000

        if mineral_numero_2.get_radioactivite() == True:
            point_mineral_2 += 1000

        if mineral_numero_1 is Metal:
            point_mineral_1 += mineral_numero_1.get_valeur() * 5

        if mineral_numero_2 is Metal:
            point_mineral_2 += mineral_numero_2.get_valeur() * 5

        if mineral_numero_1 is Gemme:
            match mineral_numero_1.get_clarte():
                case "IF":
                    point_mineral_1 += 100

                case "VVS":
                    point_mineral_1 += 70

                case "VS":
                    point_mineral_1 += 50

                case "SI":
                    point_mineral_1 += 20

        if mineral_numero_2 is Gemme:
            match mineral_numero_2.get_clarte():
                case "IF":
                    point_mineral_2 += 100

                case "VVS":
                    point_mineral_2 += 70

                case "VS":
                    point_mineral_2 += 50

                case "SI":
                    point_mineral_2 += 20

        if point_mineral_1 > point_mineral_2:
            return mineral_numero_1, mineral_numero_2, point_mineral_1, point_mineral_2, f"\nLe {mineral_numero_1.get_nom()} ({mineral_numero_1.get_numero()}) a battu le {mineral_numero_2.get_nom()} ({mineral_numero_2.get_numero()}) de {point_mineral_1 - point_mineral_2} points"

        elif point_mineral_2 > point_mineral_1:
            return mineral_numero_2, mineral_numero_1, point_mineral_2, point_mineral_1, f"\nLe {mineral_numero_2.get_nom()} ({mineral_numero_2.get_numero()}) a battu le {mineral_numero_1.get_nom()} ({mineral_numero_1.get_numero()}) de {point_mineral_2 - point_mineral_1} points"

        else:
            return mineral_numero_1, mineral_numero_2, point_mineral_1, point_mineral_2, f"\nLe {mineral_numero_1.get_nom()} ({mineral_numero_1.get_numero()}) a une force égale au {mineral_numero_2.get_nom()} ({mineral_numero_2.get_numero()}) à {point_mineral_1} points"
