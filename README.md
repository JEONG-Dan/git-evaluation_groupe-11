# Projet Git - Groupe 11
Dan JEONG

## Table des matières

* [Installation](#installation)
* [Exécution](#exécution)
    * [Mode interactif](#mode-interactif)
    * [Mode STDIN](#mode-stdin)
    * [Generator](#generator)
* [Remarques](#remarques)

## Installation

J'ai choisi de réaliser ce projet en python (version 3.13), pour la simplicité ainsi que ma maitrise du langage, bien que la boucle for me soit insupportable. 

1. **Clonez le dépôt :**
Il faudra commencer par cloner le repository.
  ```bash
  git clone https://github.com/JEONG-Dan/git-evaluation_groupe-11
  cd projet-minitrice
  ```

2. **Installez python3**
Il faut commencer par installer python3 si ce n'est pas déjà fait.

Sur windows, il faudra installer la dernière version de python sur le site officiel. 
Sur linux, il suffit d'entrer une ligne de commande selon les distribution.
* sur Ubuntu/Debian/Mint :
```bash
sudo apt install python3
```

3. **Rendez les fichiers exécutables**
Ayant travaillé sur une machine windows, il est possible que l'ajout du droit d'execution soit attendu sur une machine linux.
Pour ce faire, il suffit simplement d'entrer la commande :
```bash
chmod +x nom_du_fichier.py
```

4. **Remarques**
Je n'ai pas inclu de shebang sur les fichiers, mais étant donné que tous les fichiers ont l'extension .py, cela devrait fonctionner.

Sinon, il faudra tout simplement ajouter au début du code :
```python
#!/usr/bin/env python3
```
ou alors exécuter le programme avec python directement.

Le projet est maintenant prêt à être utilisé.

## Exécution

Le projet contient deux programmes principaux :
* minitrice.py qui est la calculatrice
* generator.py qui génère les calculs à effectuer.

### Mode interactif

Vous pouvez utiliser :
```bash
./minitrice.py
```
ou
```bash
python minitrice.py
```
(Je recommande la deuxième version)
Pour démarer le programme. 
Ensuite vous pouvez entrer différents calculs.
Pour finir le programme, vous pouvez appuyer sur Ctrl+"D".

### Mode STDIN

Le programme minitrice peut lire depuis l'entrée standard, ce qui le permet d'être piped avec d'autres commandes.

Exemple avec echo :
```bash
echo 3+9 | python minitrice.py
```

Exemple avec un fichier :
```bash
type test\00-addition.txt | python minitrice.py
```

### Generator
Le programme comprend un générateur d'expression aléatoire qu'on peut combiner avec minitrice.
Pour l'utiliser vous pouvez entrer :
```bash
python generator.py | python minitrice.py
```

## Remarques
Je ne suis pas certain que tout fonctionne sur linux, car j'ai entièrement travaillé sur une version windows. Le commandes de test aussi étaient différents, mais normalement je me suis pas trompé sur ça.