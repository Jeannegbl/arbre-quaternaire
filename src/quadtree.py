from __future__ import annotations

import json


class QuadTree:
    NB_NODES: int = 4

    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree, bg: bool | QuadTree):
        self._depth = 0
        self._nb = 0

    @property
    def depth(self) -> int:
        """ Recursion depth of the quadtree"""
        return self._depth

    @depth.setter
    def depth(self, value):
        self._depth = value

    @property
    def nb(self) -> int:
        """ Recursion depth of the quadtree"""
        return self._nb

    @nb.setter
    def nb(self, value):
        self._nb = value

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
        if QuadTree.nb > QuadTree.depth:
            QuadTree.depth = QuadTree.nb
        for i in range(len(data)):
            if type(data[i]) is list:
                QuadTree.nb += 1
                QuadTree.from_list(data[i])
        QuadTree.nb -= 1


class TkQuadTree(QuadTree):
    def paint(self):
        """ TK representation of a Quadtree"""
        pass
