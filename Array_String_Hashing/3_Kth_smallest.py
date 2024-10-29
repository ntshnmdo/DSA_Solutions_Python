def kth_smallest(self, arr, l, r, k):
    arr.sort()
    return arr[k-1]