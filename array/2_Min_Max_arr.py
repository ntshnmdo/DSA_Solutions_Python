def getMinMax(arr):
	arr.sort()
	minmax = {"min": arr[0], "max": arr[-1]}
	return minmax

arr = [1000, 11, 445, 1, 330, 3000]
minmax = getMinMax(arr)

print("Minimum element is", minmax["min"])
print("Maximum element is", minmax["max"])
