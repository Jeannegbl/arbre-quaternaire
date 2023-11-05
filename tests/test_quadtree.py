import os
import sys

from src import QuadTree

sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

QuadTree.noeud = [1]
QuadTree.decompte = 1


def test_sample():
    filename = "files/quadtree.json"
    assert QuadTree.from_file(filename) == 4


def test_single():
    filename = "files/quadtree_easy.json"
    QuadTree.from_file(filename)
    assert QuadTree.from_file(filename) == 1
