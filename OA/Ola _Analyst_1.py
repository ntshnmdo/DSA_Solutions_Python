from collections import Counter

def max_possible_arrangement(boxes):

    n = len(boxes) // 2 # since we have 2*N boxes
    count = Counter(boxes) # count the frequency of the chocolate count
    max_pairs = 0

    # try to create as many pairs as possible
    for chocolates, freq in count.items():
        # the number of pairs we can form is freq // 2
        max_pairs += freq // 2

    return min(max_pairs, n)
