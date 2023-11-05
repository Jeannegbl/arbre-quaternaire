import os
import sys

from src import QuadTree, RunTkQuadTree

sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))


def quadtree():
    filename = "files/quadtree.json"
    QuadTree.from_file(filename)


def affichage():
    RunTkQuadTree.run()


if __name__ == "__main__":
    QuadTree.noeud = [1]
    QuadTree.decompte = 1

    quadtree()
    affichage()
