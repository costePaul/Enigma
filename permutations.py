import math
from cracking import *
import logging

def permute(objects_list):
    results_map = {}
    do_permute(results_map, objects_list, [])
    return results_map

def do_permute(results_map, objects_list, permutation):
    nb_objects = len(objects_list)
    if nb_objects == 0:
        # fin de branche, on a tout permuté
        cle_finale = permutation_to_string(permutation)
        results_map[cle_finale] = permutation
    else:
        for i in range(nb_objects):
            for j in range(i+1, nb_objects):

                # calcule la sous liste
                sub_map = objects_list[:i] + objects_list[i + 1:j] + objects_list[j + 1:]

                # calcule la permutation
                permutation_tmp = []
                if len(permutation) > 0:
                    permutation_tmp = permutation.copy()
                permutation_tmp.append([objects_list[i], objects_list[j]])

                # permute la sous liste
                do_permute(results_map, sub_map, permutation_tmp)


# converti une liste en une string ordonnée
def permutation_to_string(permutation):
    key = ""
    key_parts = []
    for k in permutation:
        k0 = str(k[0])
        k1 = str(k[1])
        # tri
        if k0 > k1:
            k_tmp = k0
            k0 = k1
            k1 = k_tmp
        key_parts.append(k0 + k1)

    key_parts.sort()

    for k in key_parts:
        key += str(k) + "."
    return key


def test_permute(objects_list):
    # permute
    results_map = permute(objects_list)
    # nb found
    nb_found = len(results_map)
    # nb expected
    n = len(objects_list)
    k = n/2
    nb_expected = math.factorial(n) / (math.pow(2, k) * math.factorial(k))
    # bilan
    if nb_expected == nb_found:
        logging.info("Succes : nb solutions = " + str(nb_found))
    else:
        logging.error("Echec : expected = " + str(nb_expected) + " != found = " + str(nb_found))


def run_tests():
    test_permute(["A", "B"])
    test_permute(["A", "B", "C", "D"])
    test_permute(["A", "B", "C", "D", "E", "F"])
    test_permute(["A", "B", "C", "D", "E", "F", "G", "H"])


# run_tests()

def full_decode_repet(list_messages):  # list msg: liste de str de msg en xyzxyz du meme jour
    couple = gd_decode_repet(list_messages)
    donnee = couple[1]
    trad = couple[0]
    nb_msg = len(trad)
    if nb_msg == 1:
        print("un seul message")
        return donnee
    else:
        if len(trad[0]) >= len(trad[1]):
            ind_ref = 0
        else:
            ind_ref = 1
        for indice in range(2, nb_msg):
            if len(trad[ind_ref]) < len(trad[indice]):
                ind_ref = indice
        nb_max_posi = len(trad[ind_ref])
        compte = [0] * nb_max_posi
        for indice_trad in range(nb_max_posi):
            for i in range(nb_msg):
                for j in range(len(trad[i])):
                    if trad[i][j] == trad[ind_ref][indice_trad]:
                        compte[indice_trad] += 1
        list_sett = []
        for indice_trad in range(nb_max_posi):
            if compte[indice_trad] == nb_msg:
                list_sett.append([trad[ind_ref][indice_trad], donnee[ind_ref][indice_trad]])
        for sett in list_sett:
            check = check6(sett[0], sett[1][0], sett[1][1])
            if check[0]:
                return sett[1]