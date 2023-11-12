import os
import sys
import unittest

from src import QuadTree

sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))


class TestQuadTree(unittest.TestCase):
    """ Lancement des tests.

    Args:
        unittest.TestCase:
    Methods:
        test_sample: Vérifie si la profondeur du fichier QuadTree 'files/quadtree.json' récupéré est bien de 4.
        test_single: Vérifie si la profondeur du fichier QuadTree 'files/quadtree_easy.json' récupéré est bien de 1.
        test_error: Vérifie si le QuadTree du fichier 'files/quadtree_error.json' retourne bien une erreur.
    """
    def test_sample(self):
        """ Vérifie si la profondeur du fichier QuadTree 'files/quadtree.json' récupéré est bien de 4. """
        filename = "files/quadtree.json"
        self.assertEqual(QuadTree.from_file(filename), 4)

    def test_single(self):
        """ Vérifie si la profondeur du fichier QuadTree 'files/quadtree_easy.json' récupéré est bien de 1. """
        filename = "files/quadtree_easy.json"
        QuadTree.from_file(filename)
        self.assertEqual(QuadTree.from_file(filename), 1)

    def test_error(self):
        """ Vérifie si le QuadTree du fichier 'files/quadtree_error.json' retourne bien une erreur. """
        filename = "files/quadtree_error.json"
        with self.assertRaises(ValueError):
            QuadTree.from_file(filename)
