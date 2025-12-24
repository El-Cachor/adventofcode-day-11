import os
import numpy as np
from pathlib import Path

def creation_dico(fichier_txt):
    a=Path(__file__).resolve().parent
    b=a/fichier_txt
    dico={}
    a=open(b,'r',encoding='utf-8')
    for lignes in a:
        c=lignes.split(":")
        d=c[1].split()
        dico[c[0]]=d
    dico['out']=[]
    return dico

def matrice_adjacence(fichier_txt):
    dico=creation_dico(fichier_txt)
    dico2={}
    l=len(dico)
    L=[]
    M=np.zeros((l,l))
    k=0
    for i in dico:
        L.append((i,k))
        dico2[k]=dico[i]
        k=k+1
    for i in dico2.keys():
        for j in range(len(dico2[i])):
            dico2[i][j]=sommet_vers_nombre(L,dico2[i][j])
    for i in range(len(M)):
        for j in range(len(M)):
            if j in dico2[i]:
                M[i][j]=1
    return M,L

def nombre_sommets(fichier_txt):
    dico=creation_dico(fichier_txt)
    s=set()
    for k in dico.values():
        for i in k:
            s.add(i)
    return len(s)

def sommet_vers_nombre(L,sommet):
    for k in range(len(L)):
        if L[k][0]==sommet:
            return L[k][1]

def nombre_de_chemins(graphe):
    M,L=graphe
    you=sommet_vers_nombre(L,'you')
    out=sommet_vers_nombre(L,'out')
    m=0
    A=[]
    for k in range(1,len(M)):
        A=np.linalg.matrix_power(M,k)
        m=m+A[you][out]
    return int(m)

def nombre_de_chemins_partie_2(graphe):
    memoisation={}
    def parcours_en_profondeur_partie_2(sommet,dac,fft):
       if sommet=="dac":
            dac=True
       if sommet=="fft":
            fft=True
       etat=(sommet,dac,fft)
       if etat in memoisation:
            return memoisation[etat]
       if sommet=="out":
            if (dac and fft) is True:
                resultat=1
            else:
                resultat=0
            memoisation[etat]=resultat
            return resultat
       total=0
       for voisin in graphe.get(sommet,[]):
            total=total+parcours_en_profondeur_partie_2(voisin,dac,fft)
       memoisation[etat]=total
       return total
    return parcours_en_profondeur_partie_2("svr",False,False)

