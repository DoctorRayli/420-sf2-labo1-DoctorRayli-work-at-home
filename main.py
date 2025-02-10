import random
from caracteristique_mineraux.couleur import CouleurRGB
from caracteristique_mineraux.mineral import Mineral
from caracteristique_mineraux.gemme import Gemme
from caracteristique_mineraux.metal import Metal
from caracteristique_mineraux import fonctions_mineraux
from caracteristique_collections.collection import Collection
from caracteristique_collections import fonctions_collections
from caracteristique_mineraux.log_combat import LogCombat
from fonctions_generales.menu_principal import menu_principal as menu
from fonctions_generales.quitter import quitter

'''combat mineraux'''

if __name__ == "__main__":

    '''fonction main'''

    programme = True
   
    #Ces minéraux ont été décrits par ChatGPT
    mineraux = [
        Mineral(numero=1, nom="Quartz", formule_chimique="SiO2", couleur=CouleurRGB(r=220, g=220, b=220), lustre="Vitreux", radioactivite=False, durete=7, masse_volumique=2.65),
        Mineral(2, "Feldspath", "KAlSi3O8", CouleurRGB(255, 255, 255), "Nacré à vitreux", False, 6, 2.56),
        Mineral(3, "Gypse", "CaSO4·2H2O", CouleurRGB(255, 255, 200), "Soyeux", False, 2, 2.32),
        Mineral(4, "Calcite", "CaCO3", CouleurRGB(255, 255, 150), "Vitreux", False, 3, 2.71),
        Mineral(5, "Halite", "NaCl", CouleurRGB(255, 255, 0), "Vitreux", False, 2.5, 2.16),
        Mineral(6, "Magnétite", "Fe3O4", CouleurRGB(0, 0, 0), "Métallique", False, 5.5, 5.18),
        Mineral(7, "Pyrite", "FeS2", CouleurRGB(255, 200, 50), "Métallique", False, 6, 5.02),
        Mineral(8, "Fluorite", "CaF2", CouleurRGB(140, 255, 170), "Vitreux", False, 4, 3.18),
        Mineral(9, "Hématite", "Fe2O3", CouleurRGB(150, 0, 0), "Métallique", False, 5.5, 5.26),
        Mineral(10, "Biotite", "K(Fe, Mg)3AlSi3O10(OH, F)2", CouleurRGB(0, 0, 0), "Vitreux", False, 2.5, 3.04),
        Mineral(11, "Talc", "Mg3Si4O10(OH)2", CouleurRGB(200, 200, 255), "Cireux", False, 1, 2.75),
        Mineral(12, "Orthoclase", "KAlSi3O8", CouleurRGB(255, 200, 100), "Vitreux", False, 6, 2.56),
        Mineral(13, "Sphalérite", "ZnS", CouleurRGB(0, 0, 0), "Adamantine", False, 3.5, 4.02),
        Mineral(14, "Muscovite", "KAl2(AlSi3O10)(F, OH)2", CouleurRGB(255, 255, 200), "Vitreux", False, 2.5, 2.88),
        Mineral(15, "Cassitérite", "SnO2", CouleurRGB(0, 0, 0), "Adamantine", False, 6.5, 7.05),
        Mineral(16, "Barytine", "BaSO4", CouleurRGB(255, 255, 200), "Vitreux", False, 3, 4.48),
        Mineral(17, "Azurite", "Cu3(CO3)2(OH)2", CouleurRGB(0, 0, 255), "Vitreux", False, 4, 3.77),
        Mineral(18, "Malachite", "Cu2CO3(OH)2", CouleurRGB(0, 150, 0), "Vitreux", False, 4, 4.03),
        Mineral(19, "Apatite", "Ca5(PO4, CO3)6(F, Cl, OH)2", CouleurRGB(255, 200, 150), "Vitreux", False, 5, 3.18),
        Mineral(20, "Uraninite", "UO2", CouleurRGB(0, 0, 0), "Métallique", True, 6, 0.63),
        Mineral(21, "Torbernite", "Cu(UO2)2(PO4)2·8H2O", CouleurRGB(0, 255, 0), "Radiant", True, 2, 3.18),
        Mineral(22, "Pechblende", "U3O8", CouleurRGB(0, 0, 0), "Sub-métallique à huileux", True, 6, 0.63),
        Mineral(23, "Thorite", "ThSiO4", CouleurRGB(255, 0, 0), "Transparent à translucide", True, 4, 4.44),
        Mineral(24, "Carnotite", "K2(UO2)2(VO4)2·3H2O", CouleurRGB(255, 200, 0), "Terreux", True, 2.5, 4.9),
        Mineral(25, "Spaghetti Monster", "Sg9Bv2To5(C6H10O5)11(C6H8O7)4", CouleurRGB(255, 20, 0), "Huileux", True, 11, 32),
        Metal(numero=26, nom="Cuivre", formule_chimique="Cu", couleur=CouleurRGB(r=200, g=100, b=50), lustre="Métallique", radioactivite=False, durete=3, masse_volumique=8.96, conductivite=5.8e7, valeur=10),
        Metal(27, "Or", "Au", CouleurRGB(255, 215, 0), "Métallique", False, 5, 19.3, 4.1e7, 80_000),
        Metal(28, "Aluminium", "Al", CouleurRGB(169, 169, 169), "Métallique", False, 1.5, 2.7, 3.5e7, 3),
        Metal(29, "Fer", "Fe", CouleurRGB(169, 169, 169), "Métallique", False, 4, 7.8, 1.0e7, 0.25),
        Metal(30, "Argent", "Ag", CouleurRGB(192, 192, 192), "Métallique", False, 2.5, 10.5, 6.3e7, 974),
        Metal(31, "Zinc", "Zn", CouleurRGB(186, 196, 200), "Métallique", False, 2.5, 7.134, 1.66e7, 2.57),
        Metal(32, "Étain", "Sn", CouleurRGB(205, 205, 205), "Métallique", False, 7, 7.3, 231.9, 2.2e-5),
        Gemme(numero=33, nom="Grenat", formule_chimique="X3Y2(SiO4)3", couleur=CouleurRGB(r=200, g=0, b=0), lustre="Vitreux", radioactivite=False, durete=7, masse_volumique=4.32, clarte='VSS'),
        Gemme(34, "Diamant", "C", CouleurRGB(255, 255, 255), "Adamantin", False,  10, 3.52, "IF"),
        Gemme(35, "Saphir", "Al2O3", CouleurRGB(0, 0, 255), "Vitreux", False,  9, 3.98, "VVS"),
        Gemme(36, "Rubis", "Al2O3", CouleurRGB(255, 0, 0), "Vitreux", False,  9, 3.98, "SI"),
        Gemme(37, "Émeraude", "Be3Al2(SiO3)6", CouleurRGB(0, 255, 0), "Vitreux", False,  8, 2.76, "I"),
    ]

    '''liste de collections'''
    collections = [
        Collection(mineraux=[mineraux[19], mineraux[20], mineraux[21], mineraux[22], mineraux[23]], proprietaire="Raymond Li", nom="Dangerous Boys"),
        Collection([mineraux[24]], "Sébastien Vigneault", "Pastafarisme")
    ]

    '''liste de combats'''
    log_combat = []

    '''programme principal'''
    while programme == True:
        entree_valide = False

        print(menu())
        choix = input("\nVotre choix: ")

        match choix:
            case "1":
                print(Mineral.liste_mineraux(mineraux))

            case "2":
                print(f"\n{str(fonctions_mineraux.choix_mineraux(entree_valide, mineraux))}")

            case "3":
                print(fonctions_mineraux.masse_volume(fonctions_mineraux.choix_mineraux(entree_valide, mineraux), int(input("Voulez-vous calculer sa masse à partir du volume (1) ou calculer le volume à partir de la masse (2)? "))))

            case "4":
                gagnant, perdant, type_victoire, texte = Mineral.combat_de_mineraux(fonctions_mineraux.choix_mineraux(entree_valide, mineraux), fonctions_mineraux.choix_mineraux(entree_valide, mineraux))
                log_combat.append(LogCombat(gagnant, perdant, type_victoire))
                print(texte)

            case "5":
                gagnant, perdant, type_victoire, texte = Mineral.combat_de_mineraux(mineraux[random.randint(0,len(mineraux) - 1)], mineraux[random.randint(0,len(mineraux) - 1)])
                log_combat.append(LogCombat(gagnant, perdant, type_victoire))
                print(texte)

            case "6":
                print(fonctions_mineraux.voir_combat(log_combat))

            case "7":
                print(f"{str(fonctions_collections.choix_collection(entree_valide, collections))}")

            case "8":
                print(fonctions_collections.choix_collection(entree_valide, collections).ajout_de_mineral(fonctions_mineraux.choix_mineraux(entree_valide, mineraux)))

            case "9":
                print(fonctions_collections.choix_collection(entree_valide, collections).plus_grande_puissance())

            case "10":
                nom, proprietaire, mineraux_collection = fonctions_collections.collect_information_collection(mineraux)
                collections = Collection.creation(collections, nom, proprietaire, mineraux_collection)
                print(f"La collection {nom} de {proprietaire} qui contient les minéraux: {[x.get_nom() for x in mineraux_collection]}, à été créée")

            case "11":
                programme = quitter(programme)

            case _:
                print("\nCe n'est pas une option, veuillez réessayer")
               