'''
Generate permutations, combinations etc.
'''
from itertools import combinations, permutations, product
list(permutations([1, 2, 3], 2)) #for A(3,2)
list(combinations([1, 2, 3], 2)) #for C(3,2)
list(product([[1, 2, 3],[4,4]]))
