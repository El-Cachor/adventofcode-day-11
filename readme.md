Pour que le programme fonctionne il faut mettre tous les fichiers dans le même dossier.

Partie 1 du problème :

  L'ai utilisé le fait que l'exponentiation d'une matrice d'adjacence permet de compter le nombre de chemins entre un sommet et un autre en choisisant le nombre de sommets entre les deux.
  Le graphe étant orienté et vu la nature du problème on est sûr qu'il n'y a pas de boucle et qu'un chemin sera au maximum de la taille du nombre de sommets total.

Partie 2 du problème :

  J'ai du cette fois ci faire un parcours en profondeur car ma méthode avec la matrice d'adjacence ne permet pas de savoir quels sont les chemins qu'on emprunte. 
  Pour que le programme marche sur un gros graphe j'ai fait de la mémoïsation pour ne pas passer par des bouts de chemin en double.
