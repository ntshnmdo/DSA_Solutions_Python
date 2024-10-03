class solution:
    def removeDuplicates(self, s: str) -> str:

        res = []
        for item in s:
            if res and res[-1] == item:
                res.pop()
            else:
                res.append(item)
        return "".join(res)
                       