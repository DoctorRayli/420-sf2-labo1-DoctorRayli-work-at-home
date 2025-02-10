from caracteristique_mineraux.mineral import Mineral
from caracteristique_mineraux.gemme import Gemme
from caracteristique_mineraux.metal import Metal


def combat_de_mineraux(mineral_numero_1:object, mineral_numero_2:object):

        '''
        Cette fonction détermine le gagnant, le perdant et le type de victoire d'un combat de 2 minéraux
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
            



        '''
        if mineral_numero_1.__radioactivite == True and mineral_numero_2.__radioactivite == False:
            return mineral_numero_1, mineral_numero_2, "radioactif", f"\nLe {mineral_numero_1.get_nom()} ({mineral_numero_1.get_numero()}) a battu le {mineral_numero_2.get_nom()} ({mineral_numero_2.get_numero()}) car il est radioactif"
       
        elif mineral_numero_1.__radioactivite == False and mineral_numero_2.__radioactivite == True:
            return mineral_numero_2, mineral_numero_1, "radioactif", f"\nLe {mineral_numero_2.get_nom()} ({mineral_numero_2.get_numero()}) a battu le {mineral_numero_1.get_nom()} ({mineral_numero_1.get_numero()}) car il est radioactif"
       
        else:
            if mineral_numero_1.__durete > mineral_numero_2.__durete:
                return mineral_numero_1, mineral_numero_2, "plus dur", f"\nLe {mineral_numero_1.get_nom()} ({mineral_numero_1.get_numero()}) a battu le {mineral_numero_2.get_nom()} ({mineral_numero_2.get_numero()}) car il est plus dur"
       
            elif mineral_numero_1.__durete < mineral_numero_2.__durete:
                return mineral_numero_2, mineral_numero_1, "plus dur", f"\nLe {mineral_numero_2.get_nom()} ({mineral_numero_2.get_numero()}) a battu le {mineral_numero_1.get_nom()} ({mineral_numero_1.get_numero()}) car il est plus dur"
       
            else:
                if mineral_numero_1.__masse_volumique > mineral_numero_2.__masse_volumique:
                    return mineral_numero_1, mineral_numero_2, "plus dense", f"\nLe {mineral_numero_1.get_nom()} ({mineral_numero_1.get_numero()}) a battu le {mineral_numero_2.get_nom()} ({mineral_numero_2.get_numero()}) car il est plus dense"
       
                elif mineral_numero_1.__masse_volumique < mineral_numero_2.__masse_volumique:
                    return mineral_numero_2, mineral_numero_1, "plus dense", f"\nLe {mineral_numero_2.get_nom()} ({mineral_numero_2.get_numero()}) a battu le {mineral_numero_1.get_nom()} ({mineral_numero_1.get_numero()}) car il est plus dense"
       
                else:
                    if mineral_numero_1.__couleur.get_g() > mineral_numero_2.__couleur.get_g():
                        return mineral_numero_1, mineral_numero_2, "plus vert", f"\nLe {mineral_numero_1.get_nom()} ({mineral_numero_1.get_numero()}) a battu le {mineral_numero_2.get_nom()} ({mineral_numero_2.get_numero()}) car il est plus vert"
                   
                    elif mineral_numero_1.__couleur.get_g() < mineral_numero_2.__couleur.get_g():
                        return mineral_numero_2, mineral_numero_1, "plus vert", f"\nLe {mineral_numero_2.get_nom()} ({mineral_numero_2.get_numero()}) a battu le {mineral_numero_1.get_nom()} ({mineral_numero_1.get_numero()}) car il est plus vert"
       
                    else:
                        if mineral_numero_1.__couleur.get_b() > mineral_numero_2.__couleur.get_b():
                            return mineral_numero_1, mineral_numero_2, "plus bleu", f"\nLe {mineral_numero_1.get_nom()} ({mineral_numero_1.get_numero()}) a battu le {mineral_numero_2.get_nom()} ({mineral_numero_2.get_numero()}) car il est plus bleu"
                   
                        elif mineral_numero_1.__couleur.get_b() < mineral_numero_2.__couleur.get_b():
                            return mineral_numero_2, mineral_numero_1, "plus bleu", f"\nLe {mineral_numero_2.get_nom()} ({mineral_numero_2.get_numero()}) a battu le {mineral_numero_1.get_nom()} ({mineral_numero_1.get_numero()}) car il est plus bleu"
                   
                        else:
                            if mineral_numero_1.__couleur.get_r() > mineral_numero_2.__couleur.get_r():
                                return mineral_numero_1, mineral_numero_2, "plus rouge", f"\nLe {mineral_numero_1.get_nom()} ({mineral_numero_1.get_numero()}) a battu le {mineral_numero_2.get_nom()} ({mineral_numero_2.get_numero()}) car il est plus rouge"
                   
                            elif mineral_numero_1.__couleur.get_r() < mineral_numero_2.__couleur.get_r():
                                return mineral_numero_2, mineral_numero_1, "plus rouge", f"\nLe {mineral_numero_2.get_nom()} ({mineral_numero_2.get_numero()}) a battu le {mineral_numero_1.get_nom()} ({mineral_numero_1.get_numero()}) car il est plus rouge"
                   
                            else:
                                return mineral_numero_2, mineral_numero_1, "égalité", f"\nIl y a une égalité entre le {mineral_numero_1.get_nom()} et le {mineral_numero_2.get_nom()}"
                           '''
        