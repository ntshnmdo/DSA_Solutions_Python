def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    arr[:] = arr[-k:] + arr[:-k]

arr = [1, 2, 3, 4, 5]
k = 2
rotate_array(arr, k)
print("Rotate array:", arr)