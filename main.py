import itertools
# itertools.combinations(range(n),k)
# itertools.permutations(range(n))
from utils import *
from components import codage # demands that permutations_reflecteur.txt and permutations_rotors.txt exists
list_placement = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]

# Reflector = UKW B
permutation_reflecteur = lettretop('YRUHQSLDPXNGOKMIEBFZCWVJAT')
# print(permutation_reflecteur) # (ay)(br)(cu)(dh)(eq)(fs)(gl)(ip)(jx)(kn)(mo)(tz)(vw)

plugboard = '(bq)(cr)(di)(ej)(kw)(mt)(os)(px)(uz)(gh)'

# Model = Enigma M3
rotors_formula = ['EKMFLGDQVZNTOWYHXUSPAIBRCJ','AJDKSIRUXBLHWTMCQGZNPYFVOE', 'BDFHJLCPRTXVZNYEIWGAKMUSQO','ESOVPZJAYQUIRHXLNFTGKDCMWB','VZBRGITYUPSDNHLXAWMJQOFECK','JPGVOUMFYQBENHZRDKASXLICTW','NZJHGRCXMYSWBOUFAIVLPEKQDT','FKQHTLXOCBJSPDZRAMEWNIUYGV']
permutations_rotors = [lettretop(rotor) for rotor in rotors_formula]
# print(permutations_rotors)
# ['(aeltphqxru)(bknw)(cmoy)(dfg)(iv)(jz)(s)', '(a)(bj)(cdklhup)(esz)(fixvyomw)(gr)(nt)(q)', '(abdhpejt)(cflvmzoyqirwukxsg)(n)', '(aepliywcoxmrfzbstgjqnh)(dv)(ku)', '(avoldrwfiuq)(bzksmnhyc)(egtjpx)']

cypher = 'qfbltzezumfnqrqsvezbfldxhwkfjjnbflehxdklhdssbhvahaxqglznvozftdyaejwqizpuqy'
match = 'hackday'

def decode_for_3_rotors(fiche, cypher, looking_for, rotors_to_use): 
    #find the used combination
    #fiches is the list of the possible permutation for the refector HERE MUST A ONE ELEMENT LIST
    # cypher to text to decipher, looking for the known pattern
    for placement in list_placement:
        for i in range(1, 27):
            for j in range(1, 27):
                for k in range(1, 27):
                    decod = codage(cypher, placement, ntol([i, j, k]), fiche)
                    bool, _ = test(looking_for, decod)
                    if bool:
                        print(decod)
                        print([i, j, k])
                        print(placement)
        print("next placement")
    print('the end', rotors_to_use)

#temporary
liste_3rotors_5 = list(itertools.combinations(range(5),3)) 

for rotors_to_use in liste_3rotors_5:
    _permutations_rotors = [permutations_rotors[index] for index in rotors_to_use]
    write_rotors_reflec(_permutations_rotors, permutation_reflecteur)
    decode_for_3_rotors([plugboard], cypher, match, rotors_to_use)

# def decode_for_n_rotors(fiche, cypher, looking_for):
#     n = len(permutations_rotors)
#     ref = ['I', 'II', 'III', 'IV', 'V']
#     combi = 1 # to find
#     for a in combi:
#         write_rotors_reflec()
#         decode_for_3_rotors(fiche, cypher, looking_for)
#     return 1