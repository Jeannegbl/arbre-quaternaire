import os
import sys

from src import QuadTree

sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))


def test_sample():
    filename = "../files/quadtree.json"
    q = QuadTree.from_file(filename)
    # assert q.depth == 4


def test_single():
    filename = "../files/quadtree_easy.json"
    q = QuadTree.from_file(filename)
    # assert q.depth == 1


if __name__ == "__main__":
    test_sample()
    print(QuadTree.depth)
    print("---")
    test_single()
    print(QuadTree.depth)
