from itertools import permutations

def count_valid_permutations(n):
    # generate all possible permutations of array = [1, 2, 3, 4, ...., N]
    perm_list = permutations(range(1, n+1))
    valid_count = 0

    # check each permutations for validity
    for perm in perm_list:
        is_valid = True
        for i in range(1, n+1):
            if perm[i-1] % i != 0 and i % perm[i-1] != 0:
                is_valid = False
                break
        if is_valid:
            valid_count += 1
        
    return valid_count