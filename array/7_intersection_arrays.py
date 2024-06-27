class Solution:
    def intersection(self, a, n, b, m):

        seen = set(a)

        res = []

        for i in b:
            if i in seen:
                res.append(i)
                seen.remove(i)
        return res