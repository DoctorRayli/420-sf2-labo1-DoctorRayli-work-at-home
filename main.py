import random

from caracteristique_mineraux.couleur import CouleurRGB
from caracteristique_mineraux.mineral import Mineral
from caracteristique_mineraux.gemme import Gemme
from caracteristique_mineraux.metal import Metal
from caracteristique_mineraux import fonctions_mineraux
from caracteristique_mineraux.log_combat import LogCombat

from caracteristique_collections.collection import Collection
from caracteristique_collections import fonctions_collections

from caracteristique_alliages.alliage import Alliage
from caracteristique_alliages import fonctions_alliages

from combats import combat_alliages

from fonctions_generales import validation
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
        Metal(32, "Plomb", "Pb", CouleurRGB(128, 128, 128), "Métallique", False, 1.5, 11.34, 4.8e6, 2.2),
        Metal(33, "Antimoine", "Sb", CouleurRGB(192, 192, 192), "Métallique", False, 3, 6.68, 2.5e6, 9.5),
        Metal(34, "Nickel", "Ni", CouleurRGB(192, 192, 192), "Métallique", False, 4, 8.9, 1.4e7, 18),
        Metal(35, "Chrome", "Cr", CouleurRGB(192, 192, 192), "Métallique", False, 8.5, 7.19, 7.9e6, 10),
        Metal(36, "Molybdène", "Mo", CouleurRGB(169, 169, 169), "Métallique", False, 5.5, 10.28, 2e7, 30),
        Metal(37, "Titane", "Ti", CouleurRGB(192, 192, 192), "Métallique", False, 6, 4.51, 2.4e6, 15),
        Metal(38, "Vanadium", "V", CouleurRGB(169, 169, 169), "Métallique", False, 6.7, 6.11, 4.9e6, 25),
        Metal(39, "Magnésium", "Mg", CouleurRGB(169, 169, 169), "Métallique", False, 2.5, 1.74, 2.3e7, 2.5),
        Metal(40, "Manganèse", "Mn", CouleurRGB(169, 169, 169), "Métallique", False, 6, 7.21, 6.9e6, 1.7),
        Metal(41, "Étain", "Sn", CouleurRGB(205, 205, 205), "Métallique", False, 7, 7.3, 2.2e5, 23.19),
        Metal(42, "Uranium", "U", CouleurRGB(169, 169, 169), "Métallique", True, 6, 19.1, 6.9e6, 130),
        Metal(43, "Californium", "Cf", CouleurRGB(205, 205, 205), "Métallique", True, 5, 15.1, 2.1e6, 27_000_000),
        Gemme(numero=44, nom="Grenat", formule_chimique="X3Y2(SiO4)3", couleur=CouleurRGB(r=200, g=0, b=0), lustre="Vitreux", radioactivite=False, durete=7, masse_volumique=4.32, clarte='VVS'),
        Gemme(45, "Diamant", "C", CouleurRGB(255, 255, 255), "Adamantin", False,  10, 3.52, "IF"),
        Gemme(46, "Saphir", "Al2O3", CouleurRGB(0, 0, 255), "Vitreux", False,  9, 3.98, "VVS"),
        Gemme(47, "Rubis", "Al2O3", CouleurRGB(255, 0, 0), "Vitreux", False,  9, 3.98, "SI"),
        Gemme(48, "Émeraude", "Be3Al2(SiO3)6", CouleurRGB(0, 255, 0), "Vitreux", False,  8, 2.76, "I"),
    ]

    alliages = [
        Alliage(numero=1, nom="Acier inoxydable (Inox)", metaux={mineraux[28] : 60, mineraux[34] : 25, mineraux[33] : 10, mineraux[35] : 5}),
        Alliage(2, "Laiton", {mineraux[25] : 70, mineraux[30] : 30}),
        Alliage(3, "Bronze", {mineraux[25] : 60, mineraux[40] : 30, mineraux[27] : 10}),
        Alliage(4, "Cupro-nickel", {mineraux[25] : 80, mineraux[33] : 20}),
        Alliage(5, "Duralumin", {mineraux[27] : 93, mineraux[25] : 5, mineraux[38] : 1, mineraux[39] : 1}),
        Alliage(6, "Titane grade 5", {mineraux[36] : 90, mineraux[27] : 6, mineraux[37] : 4}),
        Alliage(7, "Inconel", {mineraux[33] : 70, mineraux[34] : 15, mineraux[28] : 10, mineraux[35] : 5}),
        Alliage(8, "Monel", {mineraux[33] : 70, mineraux[25] : 30}),
        Alliage(9, "Plomb-antimoine", {mineraux[31] : 90, mineraux[32] : 10}),
        Alliage(10, "Soudure", {mineraux[31] : 70, mineraux[40] : 30}),
        Alliage(11, "Merde Radioactif", {mineraux[41] : 50, mineraux[42] : 50}),
                ]

    '''liste de collections'''
    collections = [
        Collection(mineraux=[mineraux[19], mineraux[20], mineraux[21], mineraux[22], mineraux[23], mineraux[41], mineraux[42]], proprietaire="Raymond Li", nom="Dangerous Boys"),
        Collection([mineraux[24]], "Sébastien Vigneault", "Pastafarisme"),
        Collection([mineraux[43], mineraux[44], mineraux[45], mineraux[46], mineraux[47]], "Rich person", "Roches Précieuses")
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
                print(f"\n{fonctions_mineraux.choix_mineraux(entree_valide, mineraux)}")

            case "3":
                texte, validite = validation.validation_entree_normale(input("Voulez-vous calculer sa masse à partir du volume (1) ou calculer le volume à partir de la masse (2)? "), choix)
                if validite == True:
                    print(fonctions_mineraux.masse_volume(fonctions_mineraux.choix_mineraux(entree_valide, mineraux), int(texte)))
                
                else:
                    print("Entrée invalide, veuillez réessayer (entrez un 1 ou un 2)")

            case "4":
                gagnant, perdant, point_mineral_1, point_mineral_2, texte = Mineral.combat_de_mineraux(fonctions_mineraux.choix_mineraux(entree_valide, mineraux), fonctions_mineraux.choix_mineraux(entree_valide, mineraux))
                log_combat.append(LogCombat(gagnant, perdant, point_mineral_1, point_mineral_2))
                print(texte)

            case "5":
                gagnant, perdant, point_mineral_1, point_mineral_2, texte = Mineral.combat_de_mineraux(mineraux[random.randint(0,len(mineraux) - 1)], mineraux[random.randint(0,len(mineraux) - 1)])
                log_combat.append(LogCombat(gagnant, perdant, point_mineral_1, point_mineral_2))
                print(texte)

            case "6":
                print(fonctions_mineraux.voir_combat(log_combat))

            case "7":
                print(f"{fonctions_collections.choix_collection(entree_valide, collections)}")

            case "8":
                print(fonctions_collections.choix_collection(entree_valide, collections).ajout_de_mineral(fonctions_mineraux.choix_mineraux(entree_valide, mineraux)))

            case "9":
                print(fonctions_collections.choix_collection(entree_valide, collections).plus_grande_puissance())

            case "10":
                nom, proprietaire, mineraux_collection = fonctions_collections.collect_information_collection(mineraux)
                collections = Collection.creation(collections, nom, proprietaire, mineraux_collection)
                print(f"La collection {nom} de {proprietaire} qui contient les minéraux: {[x.get_nom() for x in mineraux_collection]}, à été créée")

            case "11":
                print(Alliage.liste_alliages(alliages))

            case "12":
                print(f"\n{fonctions_alliages.choix_alliage(entree_valide, alliages)}")

            case "13":
                metal = fonctions_alliages.choix_metal(entree_valide, mineraux)
                masse, validite = validation.validation_entree_normale(input(f"Combien de grammes de {metal.get_nom()} voulez-vous ajouter à l'alliage? "), choix)
                if validite == True:
                    print(fonctions_alliages.choix_alliage(entree_valide, alliages).ajout_metal(metal, int(masse)))

                else:
                    print("Entrée invalide, veuillez réessayer (entrez un chiffre positif)")

            case "14":
                alliage = fonctions_alliages.choix_alliage(entree_valide, alliages)
                metal = fonctions_alliages.choix_metal(entree_valide, mineraux)
                masse, validite = validation.validation_entree_normale(input(f"Combien de grammes de {metal.get_nom()} voulez-vous ajouter à l'alliage? "), choix)

                if validite == True:
                    print(alliage.soustrait_metal(metal, int(masse)))

            case "15":
                pass

            case "16":
                pass

            case "17":
                pass

            case "18":
                programme = quitter(programme)

            case _:
                print("\nCe n'est pas une option, veuillez réessayer")
 