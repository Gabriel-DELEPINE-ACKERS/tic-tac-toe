from tkinter import StringVar

# La fenêtre principale doit être initialisée avant de créer des variables liées à Tkinter
def initialize_data(fenetre):
    nom_joueur = StringVar(fenetre)  # Passe la fenêtre comme argument
    liste_joueur = []
    return nom_joueur, liste_joueur
