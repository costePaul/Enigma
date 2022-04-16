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

def create_3_among_5_list():
    # k=3 is fixed
    # n = len(liste) # n=5
    output = []
    # liste = np.arange(1,5).tolist()
    output = [[0,1,2],[1,2,3],[2,3,4],[0,1,3],[0,1,4],[0,2,3], [0,2,4], [0,3,4], [1,2,4], [1,3,4]]
    return output

# def create_3_among_8_list():
#     output = [\
#     [0,1,2], [0,1,3],[0,1,4],[0,1,5],[0,1,6],[0,1,7],\
#             [0,2,3],[0,2,4],[0,2,5],[0,2,6],[0,2,7],\
#                 [0,3,4],[0,3,5],[0,3,6],[0,3,7],\
#                     [0,4,5],[0,4,6],[0,4,7],\
#                         [0,5,6],[0,5,7],\
#                             [0,6,7],\
#         [1,2,3],[1,2,4],[1,2,5],[1,2,6],[1,2,7],\
#             [1,3,4],[1,3,5],[1,3,6],[1,3,7],\
#                 [1,4,5],[1,4,6],[1,4,7],\
#                     [1,5,6],[1,5,7],\
#                         [1,6,7],\
#         [2,3,4],[2,3,5],[2,3,6],[2,3,7],\
#             [2,4,5],[2,4,6],[2,4,7],\
#                 [2,5,6],[2,5,7],\
#                     [2,6,7],\
#         [3,4,5],[3,4,6],[3,4,7],\
#             [3,5,6],[3,5,7],\
#                 [3,6,7],\
#         [4,5,6],[4,5,7],\
#             [4,6,7],\
#         [5,6,7]]
#     return output

def create_3_among_8_list():
    # k=3 is fixed
    # n = len(liste) # n=5
    output = []
    # liste = np.arange(1,5).tolist()
    output = [[5,6,7], [4,6,7], [4,5,7], [4,5,6], [3,6,7], [3,5,7], [3,5,6],[3,4,7],[3,4,6],[3,4,5]]
    return output

# def create_3_among_n_list(n):
#     output = []
#     for i in range(1,n):
#         for j in range(i+1,n):
#             output.append([0,i,j])
#     return output

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