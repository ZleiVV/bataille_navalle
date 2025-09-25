#!/usr/bin/env python3
import random
import string
import sys

TAILLE_GRILLE = 10
COLONNES = list(string.ascii_uppercase)[:TAILLE_GRILLE]

def creer_grille_vide():
    return [[0 for _ in range(TAILLE_GRILLE)] for _ in range(TAILLE_GRILLE)]

if __name__ == '__main__':
    print("Bienvenue à la Bataille Navale")
