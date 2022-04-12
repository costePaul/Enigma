import random
from utils import *
from components import codage
list_placement = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]

# scenario 1 : we have a 6 char long message and we know it is the repetition of 3 characters, eg : abcabc
def check6(message, placement, posi):  #message: codage de "xyzxyz" donc str, placement de list_placement, posi listes de 3 chiffres
    decode = codage(message, placement, ntol(posi), [])
    m = decode[0:3]
    p = decode[3:6]
    return m == p, decode, [placement, posi]

def decode_repet(message):  # message:codage de "xyzxyz" donc str
    liste_trad = []
    liste_settings_possibles = []
    for placement in list_placement:
        for i in range(1, 27):
            for j in range(1, 27):
                for k in range(1, 27):
                    decode = check6(message, placement, [i, j, k])
                    if decode[0]:
                        liste_trad.append(decode[1])
                        liste_settings_possibles.append(decode[2])
        # print("next placement")
    return liste_trad, liste_settings_possibles  # liste de str, liste de couples

def gd_decode_repet(list_messages):
    # analyse 1er message
    trad, settings = decode_repet(list_messages[0])
    # analyse suivants
    sortie = []
    for msg in list_messages[1:]:
        for sett in settings:
            check, trad, parametre = check6(msg, sett[0], sett[1])
            if check:
                sortie.append([parametre[0], lts(ntol(parametre[1]))])
    if len(sortie) == 1:
        return sortie[0]
    else:
        return sortie

# ixidhi fiptt

mot1 = codage("abcabc", [3, 1, 2], "txp", [])
mot2 = codage("ertert", [3, 1, 2], "txp", [])
print("1: ", gd_decode_repet([mot1, mot2]))
mot1 = codage("peepee", [3, 1, 2], "txp", [])
mot2 = codage("ncinci", [3, 1, 2], "txp", [])
# print("2: ", gd_decode_repet([mot1, mot2]))
mot1 = codage("apeape", [3, 1, 2], "txp", [])
mot2 = codage("wuewue", [3, 1, 2], "txp", [])
# print("3: ", gd_decode_repet([mot1, mot2]))
mot1 = codage("ermerm", [3, 1, 2], "txp", [])
mot2 = codage("zpizpi", [3, 1, 2], "txp", [])
# print("4: ", gd_decode_repet([mot1, mot2]))
mot1 = codage("wuewue", [3, 1, 2], "txp", [])
mot2 = codage("azrazr", [3, 1, 2], "txp", [])
# print("5: ", gd_decode_repet([mot1, mot2]))
mot1 = codage("ncvncv", [3, 1, 2], "txp", [])
mot2 = codage("wxtwxt", [3, 1, 2], "txp", [])
# print("6: ", gd_decode_repet([mot1, mot2]))

def determiner_2permutations(maliste, indices):  # methode str de 6 lettres !! slmt si 2 cycles de meme longueur pour tte longueur
    separe = separe_fixe(maliste)               # indices : liste dans l'odre decroissant de taille (>=2) d'une liste
    fixe = separe[0]                            # des 2 indices des lettres qui vont ensembles
    pasfixe = classe_listes_partailles(separe[1])
    list_choix_print = []
    sortie1 = []
    sortie2 = []
    if fixe:
        sortie1.append(ntol_transpo([fixe[0][0], fixe[1][0]]))
        sortie2.append(ntol_transpo([fixe[0][0], fixe[1][0]]))
    for i in range(len(pasfixe)):
        liste = pasfixe[i]
        choix = indices[i]
        liste1 = liste[0]    # liste1 et liste2 sont les 2 cycles de meme taille associés
        liste2 = liste[1]
        taille = len(liste1)
        list_choix_print.append(("("+lts(ntol([liste[0][choix[0]], liste[1][choix[1]]]))+")"))
        for j in range(taille):
            a = (choix[0]+j) % taille
            b = (choix[1]-j) % taille
            sortie1.append(ntol_transpo([liste1[a], liste2[b]]))
        for j in range(taille):
            a = (choix[0] + j) % taille
            b = (choix[1]+1 - j) % taille
            sortie2.append(ntol_transpo([liste1[a], liste2[b]]))
    print("choix :", lts(list_choix_print))
    return sortie1, sortie2

def determiner_6permutations(maliste, list_indices):  # liste de 3 elements d'entree de det_permutation
    sortie = []
    for i in range(3):
        sortie.append(determiner_2permutations([maliste[i]], list_indices[i]))
    print("\n", "E1= ", affich_joli_permu(sortie[0][0]), "\n", "E2= ", affich_joli_permu(sortie[0][1]),
          "\n", "E3= ", affich_joli_permu(sortie[1][0]), "\n", "E4= ", affich_joli_permu(sortie[1][1]), "\n", "E5= ",
          affich_joli_permu(sortie[2][0]), "\n", "E6= ", affich_joli_permu(sortie[2][1]))

def rand_choix(maliste):  # random de choix de lettres de produits != mais de mme taille qui vont ensembles
    sortie = []
    for permu in maliste:
        sortie_temp = []
        produit = ptol(permu)
        compteur = 0
        for liste in produit:
            if compteur % 2 == 0:
                taille = len(liste)
                if taille != 1:
                    nb1 = random.randint(0, taille-1)
                    if nb1 != 0:
                        nb2 = random.randint(0, nb1-1)
                    else:
                        nb2 = random.randint(1, taille-1)
                    sortie_temp.append([nb1, nb2])
            compteur += 1
        sortie.append(sortie_temp)
    # print("\n", "choix E1E4= ", sortie[0], "\n", "choix E2E5= ", sortie[1], "\n", "choix E3E6= ", sortie[2])
    return sortie

def rand_produit(nombre_de_prod, structure=[[10, 2, 1], [6, 4, 2, 1], [5, 4, 3, 1]]):  # random de produit de compo de transpo
    sortie = []                             # somme dans une liste = 13 transpositions pour tout l'alphabet
    for i in range(nombre_de_prod):
        alphabet = get_alphabet()
        permu = ""
        structure_temp = structure[i]
        for val in structure_temp:
            for j in range(2):
                cycle = ""
                for k in range(val):
                    taille = len(alphabet)
                    indice_lettre = random.randint(0, taille-1)
                    lettre = alphabet[indice_lettre]
                    cycle += lettre
                    alphabet = alphabet.replace(lettre, "")
                permu += "("+cycle+")"
        sortie.append(permu)
    print("\n", "E1E4= ", sortie[0], "\n", "E2E5= ", sortie[1], "\n", "E3E6= ", sortie[2], "\n")
    return sortie

# E1E4 = "(dvpfkxgzyo)(eijmunqlht)(bc)(rw)(a)(s)"
# E2E5 = "(ejklmn)(ovwxyz)(fghi)(abcd)(pq)(rs)(t)(u)"
# E3E6 = "(onibu)(almep)(jzry)(vtqs)(dfg)(hkx)(c)(w)"
# listes_produit = [E1E4, E2E5, E3E6]

# listes_produit = rand_produit(3)
# choix = rand_choix(listes_produit)
# determiner_6permutations(listes_produit, choix)
