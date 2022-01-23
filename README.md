# Astrouillot_defender
par Dorian ISSELin
et Lea Colomer
https://github.com/12dorian12/Astrouillot_defender
The world is in great danger ... but Mr trouillot is here to defende it !!!! (it's a game)

## Regle du jeu 
Le but de ce jeu est de touer tout les aliens sans se faire tuer. Pour ce faire le joueur peut 
 - utiliser les touche q/d ou les fleche droite gauche pour ce deplacer sur l'écrant
 - utiliser les touche espace ou entrer pour tirer
le joueur possede trois vie, les alien tireront de facon aleatoire des laser, si le joueur en touche un il perd une vie, si il perd ces trois vie c'est la fin !
pour s'aider le joueur peut se cacher derier des mur.


## Indication

le jeu s'organise autour de 7 fichiers :
1. main.py
Il s'agit du fichier qui cree les diferentes fenetres, ainsi que les widget qui les compose et l'objet jeu
2. Jeu.py 
il permet de cree le jeu et de faire interagire les ellement qui le compose ensemble
3. Super_ad.py 
Definit une super class pour tout les element du jeu
4. Alien.py 
Permet la cration des enemie 
5. Vaisseau.py 
Permet la cration du joueur
6. ilots.py
Permet la creation des mur de protection
7. Laser.py 
Permet la creation des laser alier et ennemie


## l'implentation
- On peut retrouver l'utilisation de trois listes dans le ficher Super_ad, elles permettes de stocker les multiple objets aliens, lasers et ilots.

- on peut retrouver l'implementation d'une fonction recursive 'videur' dans le fichier jeu.py 