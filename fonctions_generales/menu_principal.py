def menu_principal() -> str:

    '''
    Cette fonction perment d'afficher le menu principal
    Elle retourne le menu sous forme de texte
    '''

    text = f"\n{100 * "="}"
    text += "\nQue voulez-vous faire?"
    text += "\n1 - Voir la liste des minéraux"
    text += "\n2 - Voir la description d'un minéral"
    text += "\n3 - Déterminer le volume ou la masse d'un minéral selon la masse ou le volume donné"
    text += "\n4 - Initier un combat entre deux minéraux de votre choix"
    text += "\n5 - Initier un combat entre deux minéraux choisi au hasard"
    text += "\n6 - Voir une liste des derniers combats"
    text += "\n7 - Afficher les détails d'une collection"
    text += "\n8 - Ajouter un mineral à une collection"
    text += "\n9 - Déterminer le mineral le plus puissant d'une collection"
    text += "\n10 - Créer une collection"
    text += "\n11 - Voir la liste des alliages"
    text += "\n12 - Afficher les détails d'un alliage"
    text += "\n13 - Ajouter un métal à un alliage"
    text += "\n14 - Soustraire un métal à un alliage"
    text += "\n15 - Créer un alliage"
    text += "\n16 - Initier un combat entre deux alliages de votre choix"
    text += "\n17 - Initier un combat entre deux alliages choisi au hasard"
    text += "\n18 - Quitter le programme"
    text += f"\n{100 * "="}"
   
    return text
   