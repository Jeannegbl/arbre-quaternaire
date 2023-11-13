from __future__ import annotations
from tkinter import *

import json

ROOT = Tk()
ROOT.geometry('600x600')
TAILLE = 500

can1 = Canvas(ROOT, width=TAILLE+100, height=TAILLE+100)
can1.pack()

TABLE = [SE, SW, NW, NE]


class QuadTree:
    """ Génération d'un QuadTree par rapport à un fichier JSON.

    Attributes:
        NB_NODES: Taille de tous les noeuds d'un QuadTree. Composé de 4 éléments qui sont soit un nombre ou soit un autre noeud.
    Methods:
        from_file: Charge un fichier JSON donné.
        from_list: Génère le Quadtree selon le fichier donné.
    """
    NB_NODES: int = 4

    def __init__(self, nb, depth, decompte, noeud):
        """ Initialisation du QuadTree.

        Args:
            nb (int): Récupère la profondeur actuelle de l'élément dans le QuadTree.
            depth (int): Récupère la profondeur maximale dans tout le QuadTree.
            decompte (int): Compteur de carrés du QuadTree.
            noeud (list): Table qui récupère le nombre de "decompte" lorsque nous entrons ou sortons d'un noeud du QuadTree et permettre de connaitre le Canvas Tkinter qu'il dépend.
        """
        self._nb = nb
        self._depth = depth
        self._decompte = decompte
        self._noeud = noeud

    @staticmethod
    def from_file(filename: str) -> QuadTree:
        """ Charge un fichier JSON donné.

        Args:
            filename (str): chemin relatif du fichier JSON.

        Return:
            QuadTree: Crée le Quadtree associé selon le fichier en argument.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                QuadTree.nb = 1
                QuadTree.depth = 0
                QuadTree.decompte = 1
                QuadTree.noeud = [1]
                return QuadTree.from_list(data)
        finally:
            file.close()

    @staticmethod
    def from_list(data: list) -> QuadTree:
        """ Génère le Quadtree selon le fichier donné.

        Args:
            data (list): Récupère le contenu du fichier JSON sous forme de liste.

        Return:
            QuadTree: Retourne la profondeur du QuadTree.
        """
        if len(data) != QuadTree.NB_NODES:
            raise ValueError("Chaque noeud du QuadTree est toujours formé de 4 éléments, un élément est soit un nombre ou soit un autre noeud.")

        if QuadTree.nb > QuadTree.depth:
            QuadTree.depth = QuadTree.nb
        for i in range(len(data)):
            QuadTree.decompte += 1
            if type(data[i]) is list:
                QuadTree.noeud.append(QuadTree.decompte)

                emplacement = TABLE[i]
                booleen = 0
                nouveau = 1
                TkQuadTree.paint(emplacement, booleen, nouveau)
                QuadTree.nb += 1

                QuadTree.from_list(data[i])
            else:
                nouveau = 0
                emplacement = TABLE[i]
                if data[i] == 1:
                    booleen = 1
                    TkQuadTree.paint(emplacement, booleen, nouveau)
                else:
                    booleen = 0
                    TkQuadTree.paint(emplacement, booleen, nouveau)

        if len(QuadTree.noeud) > 1:
            QuadTree.noeud.pop()
        QuadTree.nb -= 1
        return QuadTree.depth


class TkQuadTree:
    """ Génération d'un QuadTree par rapport à un fichier JSON.

    Methods:
        paint: Représentation graphique du Quadtree avec Tkinter.
        run: Affichage graphique du Tkinter selon le QuadTree.
    """
    @staticmethod
    def paint(emplacement, booleen, nouveau):
        """ Représentation graphique du Quadtree avec Tkinter.

        Args:
            emplacement: Permets de connaitre l'emplacement du carré selon le tableau "TABLE". L'emplacement dans le Canvas est inversé par rapport à sa place réelle.
            booleen: Permets de connaitre la couleur du carré.
            nouveau: Permets de savoir si c'est un nouveau noeud composé de carré ou un simple carré.
        """
        if booleen == 1:
            color = "black"
        else:
            color = "white"

        diviser = 1
        for i in range(QuadTree.nb):
            diviser = diviser * 2

        diviser = diviser - 0.1

        if nouveau == 1:
            globals()["can"+str(QuadTree.noeud[len(QuadTree.noeud)-1])] = Canvas(globals()["can"+str(QuadTree.noeud[len(QuadTree.noeud)-2])], width=TAILLE / diviser, height=TAILLE / diviser)
            globals()["can"+str(QuadTree.noeud[len(QuadTree.noeud)-1])].place(relx=0.5, rely=0.5, anchor=emplacement)
        else:
            can = Canvas(globals()["can"+str(QuadTree.noeud[len(QuadTree.noeud)-1])], width=TAILLE / diviser, height=TAILLE / diviser, bg=color)
            can.place(relx=0.5, rely=0.5, anchor=emplacement)

    @staticmethod
    def run():
        """ Affichage graphique du Tkinter selon le QuadTree."""
        ROOT.mainloop()
