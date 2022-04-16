from utils import *

# listes
listes_rotors, liste_reflecteur, liste_reflecteur, listes_rotormiroir = build_useful_listes()

# reflecteur
def reflecteur(entree):  # S 26 ne tourne pas à chaque permutation reflecteur
    for liste in liste_reflecteur:
        if entree == liste[0]:
            return liste[1]
        if entree == liste[1]:
            return liste[0]

def reflec_fiches(entree, fiches):
    for liste in fiches:
        if entree == liste[0]:
            return liste[1]
        elif entree == liste[1]:
            return liste[0]
    return entree

# Rotors
def rotor(num, sens, entree, decalage):  # S 26 pour une liste d'entiers tourne
    c = (entree + decalage) % 26
    if c == 0:
        c = 26
    if sens > 0:
        liste_adapte = listes_rotors
    else:
        liste_adapte = listes_rotormiroir
    for liste in liste_adapte[num - 1]:
        last = len(liste) - 1
        if c == liste[last]:
            sortie = liste[0]
        for a in range(last):
            if c == liste[a]:
                sortie = liste[a + 1]
    sortie = (sortie - decalage + 26) % 26
    if sortie == 0:
        sortie = 26
    return sortie

# Enigma
def auxenigma(lettre, ordre, decal, fiches):  # lettre:str ordre:list , decal:list ,fiches:list
    (d1, d2, d3) = decal                       # reflecfiches -> rotor 3->2->1-> reflec ->1->2->3 -> reflecfiches
    (o1, o2, o3) = ordre
    z = reflec_fiches(lettre, fiches)
    a = rotor(o1, 1, z, d1)
    b = rotor(o2, 1, a, d2)
    c = rotor(o3, 1, b, d3)
    d = reflecteur(c)
    e = rotor(o3, -1, d, d3)
    f = rotor(o2, -1, e, d2)
    g = rotor(o1, -1, f, d1)
    return reflec_fiches(g, fiches)

def enigma(message, ordre, decal, fiches):  # message:str de nb ordre:list decal:list, fiches:list
    code = []
    for i in range(len(message)):
        lettre = message[i]
        if i > 0:
            decal[0] += 1
            if decal[0] == 26:
                decal[0] = 0
                decal[1] += 1
                if decal[1] == 26:
                    decal[1] = 0
                    decal[2] += 1
                    if decal[2] == 26:
                        decal[2] = 0
        code.append(auxenigma(lettre, ordre, decal, fiches))
    return lts(ntol(code))

def codage(message, liste_ordre_rotors, position_rotors, permutation_fiches):  # message:str de lettres, ordre:list, pos:str, permu:list
    fiches = grandptol(permutation_fiches)
    if len(fiches) >= 1:
        fiches = fiches[0]
    posi = lton(position_rotors)
    for i in range(len(posi)):
        posi[i] -= 1
    return enigma(lton(message), liste_ordre_rotors, posi, fiches)