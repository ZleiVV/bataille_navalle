#!/usr/bin/env python3
import random
import string
import sys

TAILLE_GRILLE = 10
COLONNES = list(string.ascii_uppercase)[:TAILLE_GRILLE]
LISTE_BATEAUX = [
    ("Porte-avions", 5),
    ("Croiseur", 4),
    ("Contre-torpilleur", 3),
    ("Sous-marin", 3),
    ("Torpilleur", 2),
]

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

def convertir_coordonnees(entree):
    entree = entree.strip().upper()
    if len(entree) < 2:
        return None
    col = entree[0]
    partie_ligne = entree[1:]
    if col not in COLONNES:
        return None
    try:
        ligne = int(partie_ligne)
    except ValueError:
        return None
    if not (1 <= ligne <= TAILLE_GRILLE):
        return None
    return (ligne - 1, COLONNES.index(col))

def peut_placer(grille, depart, taille, orientation):
    r, c = depart
    dr, dc = (0, 1) if orientation == 'H' else (1, 0)
    for i in range(taille):
        rr = r + dr * i
        cc = c + dc * i
        if not (0 <= rr < TAILLE_GRILLE and 0 <= cc < TAILLE_GRILLE):
            return False
        if grille[rr][cc] != 0:
            return False
    return True


def placer_bateau(grille, depart, taille, orientation):
    r, c = depart
    dr, dc = (0, 1) if orientation == 'H' else (1, 0)
    coords = []
    for i in range(taille):
        rr = r + dr * i
        cc = c + dc * i
        grille[rr][cc] = 'B'
        coords.append((rr, cc))
    return coords

def placement_aleatoire(grille):
    bateaux = {}
    for nom, taille in LISTE_BATEAUX:
        place = False
        while not place:
            orientation = random.choice(['H', 'V'])
            r = random.randrange(TAILLE_GRILLE)
            c = random.randrange(TAILLE_GRILLE)
            if peut_placer(grille, (r, c), taille, orientation):
                coords = placer_bateau(grille, (r, c), taille, orientation)
                bateaux[nom] = coords
                place = True
    return bateaux

def placement_manuel(grille):
    bateaux = {}
    print("Placement manuel: entrez la position de départ et l'orientation (H ou V). Exemple: A1 H")
    afficher_grille(grille, reveler=True)
    for nom, taille in LISTE_BATEAUX:
        ok = False
        while not ok:
            print(f"Placer {nom} (taille {taille}).")
            brut = input("Position (ex A1) : ").strip()
            depart = convertir_coordonnees(brut)
            if not depart:
                print("Position invalide, recommencez.")
                continue
            ori = input("Orientation H(horizontal) ou V(vertical) : ").strip().upper()
            if ori not in ('H', 'V'):
                print("Orientation invalide.")
                continue
            if peut_placer(grille, depart, taille, ori):
                bateaux[nom] = placer_bateau(grille, depart, taille, ori)
                afficher_grille(grille, reveler=True)
                ok = True
            else:
                print("Placement impossible ici. Réessayez.")
    return bateaux

# --- Code de test ---
if __name__ == "__main__":
    print("Test du placement aléatoire des bateaux :")
    ma_grille_auto = creer_grille_vide()
    bateaux_auto = placement_aleatoire(ma_grille_auto)
    afficher_grille(ma_grille_auto, reveler=True)
    print("Bateaux placés automatiquement :", bateaux_auto)

    print("\nTest du placement manuel :")
    ma_grille_man = creer_grille_vide()
    bateaux_man = placement_manuel(ma_grille_man)
    print("Bateaux placés manuellement :", bateaux_man)