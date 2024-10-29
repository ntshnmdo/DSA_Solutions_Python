def doUnion(self, a, n, b, m):

    x = []
    hashset = set()

    for i in a:
        if i not in hashset:
            x.append(i)
            hashset.add(i)
    
    for i in b:
        if i not in hashset:
            x.append(i)
            hashset.add(i)
    return len(x)