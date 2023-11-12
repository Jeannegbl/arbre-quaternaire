# QuadTree - Arbre Quaternaire

# Présentation

Un **quadtree** ou **arbre quaternaire** (arbre Q) est une structure de données de type arbre dans laquelle chaque nœud a quatre fils. Les quadtrees sont le plus souvent utilisés pour partitionner un espace bidimensionnel en le subdivisant récursivement en quatre nœuds.

Il existe plusieurs types de quadtree. Dans notre cas il s'agit d'un quadtree "region".
Le quadtree «région» représente une partition de l'espace en deux dimensions en décomposant la région en quatre quadrants égaux, puis chaque quadrant en quatre sous-quadrants, et ainsi de suite, avec chaque «nœud terminal» comprenant des données correspondant à une sous-région spécifique. Chaque nœud de l'arbre a exactement : soit quatre enfants, soit aucun (cas d'un nœud terminal).
Chaque noeud comportant quatre éléments. Il s'agit d'une technique connue pour l'encodage d'images.  Pour simplifier, les images sont carrées, de couleur noir et blanc
et de côté 2^n.

<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Quad_tree_bitmap.svg/380px-Quad_tree_bitmap.svg.png" alt="QuadTree"/>
</div>

Ce projet a pour but de générer un QuadTree par rapport à un fichier JSON donnée.

----
# Dépendances
Ce projet nécessite:
 - **Python** *3.11*:

----
# Installation
## SSH 
```shell
git clone git@github.com:Jeannegbl/arbre-quaternaire.git 
```
```shell
cd arbre-quaternaire
```
```shell
pip install -r requirements.txt
```
## HTTP
```shell
git clone https://github.com/Jeannegbl/arbre-quaternaire.git 
```
```shell
cd arbre-quaternaire
```
```shell
pip install -r requirements.txt
```

----
# Lancer les test : 
```shell
python -m pytest tests/test_quadtree.py -x
```

----
# Lancer le projet :
```
python quadtree-affichage.py
```

----
# Faire son propre QuadTree

Il est possible de créer son propre QuadTree, le fichier **files/quadtree.json** peut servir d'exemple :
````json
[
       [0,0,0,[1,0,0,0]],
       [0,0,[0,1,0,0],0],
       [0,0,0,[[1,0,0,1],[0,0,1,1],0,0]],
       [0,0,[[0,0,1,1],[0,1,1,0],0,0],0]
]
````
- Les 1 représentent les carrés noirs, les 0 sont les carrés blancs.
- Chaque noeud est toujours formé de 4 éléments, un élément est soit un nombre ou soit un autre noeud.
- Le fichier doit être au format JSON.

Il faut aussi changer le fichier à utiliser dans le fichier **quadtree-affichage.py**.
````python
def quadtree():
    filename = "files/quadtree.json"
    QuadTree.from_file(filename)
````
