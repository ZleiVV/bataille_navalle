#!/usr/bin/env python3
import random
import string
import sys

TAILLE_GRILLE = 10
COLONNES = list(string.ascii_uppercase)[:TAILLE_GRILLE]

def creer_grille_vide():
    return [[0 for _ in range(TAILLE_GRILLE)] for _ in range(TAILLE_GRILLE)]

def afficher_grille(grille, reveler=False):
    en_tete = "   " + " ".join(f"{c}" for c in COLONNES)
    print(en_tete)
    for r in range(TAILLE_GRILLE):
        numero_ligne = f"{r+1:2}"
        cases = []
        for c in range(TAILLE_GRILLE):
            case = grille[r][c]
            symbole = '~'
            if case == 0:
                symbole = '~'
            elif case == 'B':
                symbole = 'B' if reveler else '~'
            elif case == 'T':
                symbole = 'X'
            elif case == 'X':
                symbole = 'o'
            cases.append(symbole)
        print(f"{numero_ligne} " + " ".join(cases))

ma_grille = creer_grille_vide()
afficher_grille(ma_grille)

if __name__ == '__main__':
    print("Bienvenue à la Bataille Navale")