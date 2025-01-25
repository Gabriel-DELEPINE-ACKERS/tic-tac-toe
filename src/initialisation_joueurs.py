import time
from tkinter import StringVar, Button
from data import initialize_data  # Importer depuis data.py

# Fonction de validation du nom des joueurs
def player_name(label_message, nom_joueur, bouton_grille, liste_joueur):
    joueur = nom_joueur.get().strip()  # Récupérer le nom entré
    if not joueur:
        label_message['text'] = "Je crois que vous avez oublié de rentrer votre nom. Réessayez."
        return

    liste_joueur.append(joueur)
    if len(liste_joueur) == 1:
        label_message['text'] = f"Bienvenue {liste_joueur[0]} ! Veuillez entrer le nom du Joueur 2."
        nom_joueur.set("")  # Réinitialiser le champ de saisie
    elif len(liste_joueur) == 2:
        label_message['text'] = f"Bonjour {liste_joueur[0]} et {liste_joueur[1]} !"
        label_message.after(2000, lambda: label_message.config(text="Prêts à jouer ?"))
        nom_joueur.set("")  # Facultatif, pour laisser le champ vide
        print(f"Joueurs enregistrés : {liste_joueur}")
        bouton_grille.pack()  # Afficher le bouton pour la grille

# Fonction pour configurer les boutons dans la fenêtre
def setup_buttons(fenetre, label_message, liste_joueur, nom_joueur, bouton_grille):
    bouton_validation_joueur = Button(fenetre, text='Valider', command=lambda: player_name(label_message, nom_joueur, bouton_grille, liste_joueur))
    bouton_validation_joueur.pack()
