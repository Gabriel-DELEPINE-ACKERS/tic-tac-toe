# Activité Morpion avec TDD

## Description

Cette activité vous guide pour développer un jeu de Morpion entièrement fonctionnel en utilisant l'approche **Test-Driven Development (TDD)**. Vous apprendrez à :

- Créer le moteur du jeu.
- Gérer les tests unitaires pour valider chaque étape.
- Ajouter un robot joueur basique.
- Jouer des parties complètes dans le terminal.

## Objectifs pédagogiques

- Découvrir et appliquer le TDD.
- Structurer un projet avec Git.
- Développer une IA simple pour jouer contre un robot.

## Étapes principales

1. **Création de la grille** :
   - Générer une grille carrée vide de taille spécifiée.
   - Tests pour valider la création correcte de la grille.

2. **Placement des pions** :
   - Ajouter un pion sur la grille si la case est libre.
   - Tests pour valider les placements valides et les erreurs.

3. **Détection des victoires** :
   - Identifier les alignements gagnants (lignes, colonnes, diagonales).
   - Tests pour vérifier le fonctionnement.

4. **Boucle principale** :
   - Permettre à deux joueurs de jouer à tour de rôle.
   - Afficher l'état de la grille après chaque coup.

5. **Robot joueur** :
   - Le robot joue de manière stratégique :
     - Gagne si possible.
     - Défend si l'adversaire peut gagner.
     - Joue aléatoirement sinon.
   - Tests pour valider le comportement du robot.

## Utilisation

### 1. Installation

Clonez le dépôt et accédez au répertoire du projet :
```bash
git clone <lien_du_dépôt>
cd morpion_project
```

Installez les dépendances si nécessaire (Python >= 3.8 est requis).

### 2. Exécution

Pour lancer une partie dans le terminal, exécutez :
```bash
python morpion.py
```

### 3. Tests unitaires

Pour valider les fonctionnalités à chaque étape, exécutez les tests avec :
```bash
pytest tests/
```

## Structure du projet

```
.
├── morpion.py          # Contient le moteur du jeu Morpion.
├── tests/
│   ├── test_morpion.py # Tests unitaires pour les fonctionnalités du Morpion.
├── README.md           # Documentation du projet.
└── requirements.txt    # (Optionnel) Dépendances Python.
```

## Extensions possibles

- Ajouter un mode multijoueur en ligne.
- Améliorer l'IA avec l'algorithme Minimax.
- Créer une interface graphique avec Tkinter.
