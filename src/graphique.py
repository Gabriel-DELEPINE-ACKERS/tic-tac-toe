from tkinter import *
from main import create_grid
from initialisation_joueurs import setup_buttons
from data import initialize_data

fenetre = Tk()

# Initialisation des variables après la création de la fenêtre
nom_joueur, liste_joueur = initialize_data(fenetre)  # Initialiser les variables ici

# Logo en haut de la fenetre
img_logo = PhotoImage(file=r'C:\Users\User\Gabriel\Cours\Cours de terminal\NSI\projet_console\Logo_console.png')
fenetre.iconphoto(False, img_logo)

# Création de la fenêtre Menu
fenetre.geometry('600x600')
fenetre.title('Menu')
fenetre['bg'] = 'black'
fenetre.resizable(height=True, width=True)

# Ajout du logo en haut à droite
photo_logo = PhotoImage(file=r'C:\Users\User\Gabriel\Cours\Cours de terminal\NSI\projet_console\Logo_console.png')
label_photo = Label(fenetre, image=photo_logo)
label_photo.place(x='0', y='20')

label = Label(fenetre, text="Bienvenue !", font=('Verdana', 20, "bold"), fg='white', bg='black')
label.pack()

label_message = Label(fenetre, text="", font=('Verdana', 15), fg='white', bg='black')
label_message.pack()

label_joueur = Label(fenetre, text='Veuillez entrer votre nom/pseudo')
label_joueur.pack()

entree = Entry(fenetre, textvariable=nom_joueur)
entree.pack()

# Créer le bouton pour afficher la grille
bouton_grille = Button(fenetre, text='Jouer au Tic-tac-toe', bg='blue', fg='white', command=lambda: print(create_grid(3, 3)))

# Ajouter les boutons après la création de la fenêtre
from initialisation_joueurs import setup_buttons
setup_buttons(fenetre, label_message, liste_joueur, nom_joueur, bouton_grille) 



fenetre.mainloop()
