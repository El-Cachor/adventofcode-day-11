from fonction import *

if __name__ == "__main__":
    graphe = matrice_adjacence("input.txt")
    resultat = nombre_de_chemins(graphe)
    print("Nombre total de chemins de you à out :", resultat)

    graphe = creation_dico("input.txt")
    resultat = nombre_de_chemins_partie_2(graphe)
    print("Nombre de chemins de svr à out passant par dac et fft :", resultat)

