# * Jeu du pendu *
import random

from pyparsing import str_type

"""Ce module permet de fournir des fonctions pour le jeu du Pendu
Il est écrit par Marlene Sanjose dans le cadre du cours MGA802
"""


# Choisi un mot aléatoire dans un fichier
def retourner_mot(fichier="mots_pendu.txt", dossier="./ressources"):
    import os

    # teste si le fichier existe
    full_filename = os.path.join(dossier,fichier)
    if not os.path.isfile(full_filename):
        raise RuntimeError(f'Je ne trouve pas le fichier {full_filename} !')

    # Ouvre le fichier contenant les mots en mode lecture
    with open(full_filename, 'r', encoding='utf8') as f:
        # Lire le contenu du fichier
        words = f.read()

    word_list = words.split('\n')
# change les lettres avec accents par des lettres sans accent
    liste_sans_accents = []
    for i in word_list :
        i = i.replace('â','a' )
        i = i.replace('ä', 'a')
        i = i.replace('é', 'e')
        i = i.replace('è', 'e')
        i = i.replace('ë', 'e')
        i = i.replace('ê', 'e')
        i = i.replace('î', 'i')
        i = i.replace('ï', 'i')
        i = i.replace('ö', 'o')
        i = i.replace('ô', 'o')
        i = i.replace('û', 'u')
        i = i.replace('ü', 'u')
        liste_sans_accents.append(i)

    mot = random.choice(liste_mot)
    print(mot)
    return  mot

# Affiche les lettres manquantes du mot
def cacher_mot(mot) :
    pendu = '_' * len(mot)
    return pendu


#mot_cache = cacher_mot(mot)


# Vérifie si la lettre proposee appartient au mot de la liste, décompte les vies

def verifier_lettre(mot, mot_cache):
    vies = 6
    essais = []

    while vies > 0:
        lettre_propose = input('Proposez une lettre pour trouver le mot : ').lower()

#si l'utilisateur a déjà propose cette lettre, renvoie un message lui indiquant
        if lettre_propose in essais or lettre_propose in mot_cache:
            print(f'vous avez déjà essayé cette lettre : {lettre_propose}')

        trouve = False
        for i in range(len(mot)):
            if lettre_propose == mot[i]:
                mot_cache = mot_cache[:i] + lettre_propose + mot_cache[i + 1:]
                trouve = True
        print(mot_cache)

        # Ce test est exécuté une seule fois après la boucle
        if trouve == False:
            vies -= 1
            print('nombre de vie', vies)
            print("La lettre n'est pas contenue dans le mot")

            # BONUS : donne un indice dans le cas où il reste une seule vie
            if vies == 1:
                for k in mot:
                    if k not in essais:
                        indice = random.choice(mot)
                    print(f'Le mot contient la lettre :{indice}')
                    break

        if mot_cache == mot:
            print(f'tu as trouvé le mot ! :{mot_cache}')
            break

    print(vies)

    return mot_cache


#mot = 'alpha'
#mot_cache = cacher_mot(mot)
#resultat = verifier_lettre(mot, mot_cache)
#print(resultat)



# source : Cours de Marlene Sanjose, cours classe préparatoire monsieur Gergadier
