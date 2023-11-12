import os
import sys

from src import QuadTree, TkQuadTree

sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))


def quadtree():
    """Lancement du projet"""
    filename = "files/quadtree.json"
    QuadTree.from_file(filename)
    TkQuadTree.run()


if __name__ == "__main__":
    quadtree()
