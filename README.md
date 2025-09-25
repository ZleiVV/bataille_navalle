# Bataille Navale — Jeu Python

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Licence](https://img.shields.io/badge/Licence-MIT-green.svg)](LICENSE)

## Description
Ce projet est une **implémentation de la Bataille Navale** en Python, opposant un joueur humain à l’ordinateur.  
Le jeu se joue dans le terminal et inclut :

- Placement **automatique ou manuel** des bateaux.  
- Tours de jeu alternés : joueur puis ordinateur.  
- Système de tir avec résultats : **manqué, touché, coulé**.  
- Vérification automatique de la fin de partie.  
- Affichage clair des grilles pour le joueur.  
- Gestion d’une sortie propre avec `Ctrl+C`.

---

## Règles du jeu

1. Chaque joueur dispose de 5 bateaux :  
   - Porte-avions (5 cases)  
   - Croiseur (4 cases)  
   - Contre-torpilleur (3 cases)  
   - Sous-marin (3 cases)  
   - Torpilleur (2 cases)  

2. Objectif : **coul­er tous les bateaux adverses** avant que l’ordinateur ne coule les vôtres.  

3. Pendant votre tour :  
   - Entrez une coordonnée pour tirer (ex : `A5`).  
   - Tapez `q` pour quitter à tout moment.

4. L’ordinateur tire automatiquement sur des cases aléatoires non encore ciblées.

---

**Légende :**  
- `~` : case vide  
- `B` : bateau (visible uniquement sur la grille du joueur)  
- `X` : tir manqué  
- `T` : tir touché  

---

## Utilisation

- **Placement automatique** : le jeu place vos bateaux aléatoirement.  
- **Placement manuel** : vous choisissez les coordonnées et l’orientation de chaque bateau.  
- Pendant le jeu :  
  - Entrez une coordonnée pour tirer (ex : `B7`).  
  - Tapez `q` pour quitter la partie à tout moment.  
- La grille du joueur montre ses bateaux et les tirs de l’ordinateur.  
- La grille adverse montre uniquement vos tirs sur l’ennemi.
