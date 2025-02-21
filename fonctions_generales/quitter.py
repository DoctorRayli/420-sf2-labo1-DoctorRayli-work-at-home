def quitter(programme:bool) -> bool:

    '''
    Cette fonction permet de vérifier que l'utilisateur veut véritablement quitter
    Elle reçoit la variable booléenne 'programme'
    Elle retourne la variable 'programme' (si changée: l'utilisateur quitte le programme)
    '''

    quitter = input("\nÊtes-vous sûr de vouloir quitter? (oui/non): ").lower()

    if quitter != "non" and quitter != "oui":
        print("Option invalide, mais nous allons assumer que vous voulez arrêter")
        programme = False

    elif quitter == "oui":
        programme = False

    return programme
