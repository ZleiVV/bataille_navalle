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

def tirer(grille, bateaux, pos):
    r, c = pos
    val = grille[r][c]
    if val == 0:
        grille[r][c] = 'X'
        return 'manqué', None
    elif val == 'B':
        grille[r][c] = 'T'
        bateau_coule = None
        for nom, coords in bateaux.items():
            if (r, c) in coords:
                if all(grille[rr][cc] == 'T' for rr, cc in coords):
                    bateau_coule = nom
                break
        return 'touché', bateau_coule
    elif val in ('T', 'X'):
        return 'déjà', None
    return 'manqué', None

def tour_ia(grille_joueur, bateaux_joueur, memoire_ia):
    candidats = [(r, c) for r in range(TAILLE_GRILLE) for c in range(TAILLE_GRILLE) if (r, c) not in memoire_ia]
    pos = random.choice(candidats)
    memoire_ia.add(pos)
    resultat, coule = tirer(grille_joueur, bateaux_joueur, pos)
    col = COLONNES[pos[1]]
    print(f"L'ordinateur tire en {col}{pos[0]+1} -> {resultat}", end='')
    if coule:
        print(f" et coulé votre {coule} !")
    else:
        print()
    return resultat

import sys

def tour_joueur(grille_adverse, bateaux_adverses, vue_adverse):
    print("--- Votre tour ---")
    afficher_grille(vue_adverse, reveler=False)
    while True:
        brut = input("Entrez une coordonnée à tirer (ex A5) ou 'q' pour quitter: ").strip()
        if brut.lower() == 'q':
            print("A bientôt !")
            sys.exit(0)
        pos = convertir_coordonnees(brut)
        if not pos:
            print("Coordonnée invalide.")
            continue
        resultat, coule = tirer(grille_adverse, bateaux_adverses, pos)
        r, c = pos

        # Mettre à jour la vue du joueur
        if resultat == 'touché':
            vue_adverse[r][c] = 'T'
        elif resultat == 'manqué':
            vue_adverse[r][c] = 'X'

        # Messages au joueur
        if resultat == 'déjà':
            print("Vous avez déjà tiré ici.")
            continue
        elif resultat == 'manqué':
            print("Manqué !")
        elif resultat == 'touché':
            if coule:
                print(f"Touché et coulé ! Vous avez coulé le {coule}.")
            else:
                print("Touché !")
        break

# --- Code de test ---
if __name__ == "__main__":
    print("=== Test interactif des tours joueur et IA ===")
    
    # Créer les grilles et placer les bateaux
    grille_joueur = creer_grille_vide()
    bateaux_joueur = placement_aleatoire(grille_joueur)
    
    grille_adverse = creer_grille_vide()
    bateaux_adverse = placement_aleatoire(grille_adverse)
    
    vue_adverse = creer_grille_vide()
    memoire_ia = set()
    
    print("\nGrille du joueur (révélée) :")
    afficher_grille(grille_joueur, reveler=True)
    
    print("\nGrille adverse (révélée) :")
    afficher_grille(grille_adverse, reveler=True)
    
    # Jouer 3 tours interactifs pour tester
    for i in range(3):
        print(f"\n--- Tour {i+1} ---")
        tour_joueur(grille_adverse, bateaux_adverse, vue_adverse)
        tour_ia(grille_joueur, bateaux_joueur, memoire_ia)
        
        print("\nGrille du joueur après tir IA :")
        afficher_grille(grille_joueur, reveler=True)
        print("\nVue du joueur sur l'adversaire :")
        afficher_grille(vue_adverse, reveler=False)
