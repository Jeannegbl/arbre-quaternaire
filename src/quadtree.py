from __future__ import annotations
from tkinter import *

import json

ROOT = Tk()
ROOT.geometry('600x600')
TAILLE = 500

can1 = Canvas(ROOT, width=TAILLE+100, height=TAILLE+100)
can1.pack()


class QuadTree:
    NB_NODES: int = 4

    def __init__(self):
        self._depth = 0
        self._nb = 0
        self._noeud = []
        self._decompte = 0

    @staticmethod
    def from_file(filename: str) -> QuadTree:
        """ Open a given file, containing a textual representation of a list"""

        with open(filename, 'r') as file:
            data = json.load(file)
            QuadTree.nb = 1
            QuadTree.depth = 0
            return QuadTree.from_list(data)

    @staticmethod
    def from_list(data: list) -> QuadTree:
        """ Generates a Quadtree from a list representation"""
        table = [SE, SW, NW, NE]
        if QuadTree.nb > QuadTree.depth:
            QuadTree.depth = QuadTree.nb
        for i in range(len(data)):
            QuadTree.decompte += 1
            if type(data[i]) is list:
                QuadTree.noeud.append(QuadTree.decompte)

                emplacement = table[i]
                booleen = 0
                nouveau = 1
                TkQuadTree.paint(emplacement, booleen, nouveau)
                QuadTree.nb += 1

                QuadTree.from_list(data[i])
            else:
                nouveau = 0
                emplacement = table[i]
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


class TkQuadTree(QuadTree):
    @staticmethod
    def paint(emplacement, booleen, nouveau):
        """ TK representation of a Quadtree"""
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


class RunTkQuadTree:
    @staticmethod
    def run():
        ROOT.mainloop()
