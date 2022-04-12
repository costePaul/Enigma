import time
from utils import *

list_placement = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]

from components import codage

# test
list_fiches = [["(pe)"], ["(pe)(uk)"], ["(pe)(uk)(ao)(ix)(wy)(qb)"], ["(pe)(uk)(ao)(ix)(wy)(qb)(ch)(fm)(ns)(dg)"]]

def enigma_carre(message, ordre, positions, fiches):
    return codage(codage(message, ordre, positions, fiches), ordre, positions, fiches)

# print(codage("message", [2, 1, 3], "iem", ["(xp)(en)(al)(is)"]))
# print(codage("hjlievs", [2, 1, 3], "iem", ["(xp)(en)(al)(is)"]))
# print(codage("ocean", [1, 3, 2], "aaa", []))
# print(codage("ocean", [1, 3, 2], "aaa", ["(op)"]))

def test_tout(message): #brut force verification to enigma is a symmetry
    start = time.time()
    faute = False
    for placement in list_placement:
        for i in range(1, 27):
            for j in range(1, 27):
                for k in range(1, 27):
                    for fiches in list_fiches:
                        if not(enigma_carre(message, placement, ntol([i, j, k]), fiches)==message):
                            print([i, j, k])
                            print(fiches)
                            print(placement)
                            faute = True
        print("next placement")
    end = time.time()
    print(int(end - start))
    print(not faute)

test_tout("aupief")
