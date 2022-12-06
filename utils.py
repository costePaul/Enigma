import numpy as np

def get_alphabet(): # A = get_alphabet()
    return "abcdefghijklmnopqrstuvwxyz"

def get_list_alphabet(): # L = get_list_alphabet()
    return list(get_alphabet())

def ent(letter):  # converti une lettre en un entier correspondant à sa position dans l'alphabet
    return ord(letter)-97+1

def letter(i):  # converti en entier en la lettre correspondante à son % 26
    i = ((i-1)%26)+1
    return chr(i+97-1)

def lton(t):  # converti un list ou str de lettre en la liste de leurs indices respectifs
    return [ent(i) for i in t]

def lton_deeper(entree):  # run lton sur les elements d'une liste
    return [lton(val) for val in entree]

def ntol(entree):  # converti une liste de nombres entre 1 et 26 en la liste des lettres correspondantes
    return [letter(i) for i in entree]

def ntol_transpo(entree): # converti une liste de 2 nombres (donc pour une transposition) en le str de 2 lettres correspondants
    [a, b] = ntol(entree)
    return a+b

def lts(entree):  # converti une list en un str
    s = ""
    for i in entree:
        s = s + str(i)
    return s

def miroir(entree):  # renvoie une liste dont les elements sont dans l'ordre opposé
    n = len(entree)
    sortie = [0] * n
    for i in range(n):
        sortie[n - 1 - i] = entree[i]
    return sortie

def miroir_deeper(entree):  # run miroir sur les listes d'une liste
    return [miroir(entree[i]) for i in range(len(entree))]

def miroir_deepercarre(entree):  # run miroir_deeper sur les listes d'une liste :-)
    return [miroir_deeper(entree[i]) for i in range(len(entree))]

def ptol(entree):  # lis le str de permutations (en lettres avec (ab)(cd) ) et les transforme en liste (de lettres [[ab],[cd]])
    sortie = []
    for val in entree:
        if val == "(":
            liste = []
        elif val == ")":
            sortie.append(liste)
        else:
            liste.append(val)
    return sortie

def grandptol(entree):  # run ptol sur les éléments d'une liste
    return [lton_deeper(ptol(entree[i])) for i in range(len(entree))]

def test_position(t, s, p):  # t et s str, p = indice de position
    boul = True
    for i in range(0, len(t)):
        if not (s[i + p] == t[i]):
            boul = False
    return boul

def test(t, s):  # t et s str
    index = -1
    if len(s) < len(t):
        print(str(t) + " Trop long")
        return False
    boul = False
    for i in range(0, len(s) - len(t) + 1):
        if test_position(t, s, i):
            boul = True
            index=i
    return boul, index

def occurrences(t, s):  # t et s str
    liste = []
    if len(s) < len(t):
        print(str(t) + "Trop long")
        return False
    for i in range(0, len(s) - len(t) + 1):
        if test_position(t, s, i):
            liste.append(i)
    return liste

def classe_listes_partailles(liste_deliste):
    sortie = []
    dico = {}
    for liste in liste_deliste:
        taille = len(liste)
        if taille in dico:
            dico[taille].append(liste)
        else:
            dico[taille] = [liste]
    for cle in dico:
        sortie.append(dico[cle])
    return sortie

def affich_joli_permu(entree):  # liste de str de taille 2 transformees en permu ecrites mathematiquement
    sortie = ""
    for val in entree:
        sortie += "("+val+")"
    return sortie

def separe_fixe(maliste):
    liste_fixe = []
    liste_pasfixe = []
    for liste in grandptol(maliste)[0]:
        if len(liste) == 1:
            liste_fixe.append(liste)
        else:
            liste_pasfixe.append(liste)
    return liste_fixe, liste_pasfixe

def lettretop(lettres): #permutations sous la forme de 26 lettres (A...Z->lettres)
    lettres = lettres.lower()
    output = "(a"
    liste_index = np.arange(0,27)
    liste_index[1]=0
    counter = 26+1
    lettre_index = 1
    last_first_letter_index = lettre_index

    while len(output)<counter:
        # print(liste_index)
        cur_letter = lettres[lettre_index-1]
        cur_letter_index = ent(cur_letter)
        
        if cur_letter_index == last_first_letter_index:
            lettre_index = liste_index[liste_index!=0][0]
            liste_index[lettre_index]=0
            last_first_letter_index = lettre_index
            output += ')('+letter(lettre_index)
            counter += 2
        else:
            output += cur_letter
            liste_index[cur_letter_index]=0
            lettre_index = cur_letter_index
    return output+')'

def write_rotors_reflec(permutations_rotors, permutation_reflecteur):
    f_rotor = open('./permutations_rotors.txt', 'w+')
    for rotor in permutations_rotors:
        f_rotor.write(rotor+'\n')
    f_reflecteur = open('./permutations_reflecteur.txt', 'w+')
    f_reflecteur.write(permutation_reflecteur)

def build_useful_listes():
    with open('./permutations_rotors.txt', 'r') as f:
        permutations_rotors = f.read().split('\n')
    permutations_rotors = permutations_rotors[:3]
    with open('./permutations_reflecteur.txt', 'r') as f:
        permutation_reflecteur = f.read().split('\n')
    permutation_reflecteur = permutation_reflecteur[:1]

    listes_rotors = grandptol(permutations_rotors)
    liste_reflecteur = grandptol(permutation_reflecteur)
    liste_reflecteur = liste_reflecteur[0]
    listes_rotormiroir = miroir_deepercarre(listes_rotors)
    return listes_rotors, liste_reflecteur, liste_reflecteur, listes_rotormiroir