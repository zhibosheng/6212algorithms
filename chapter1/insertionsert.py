#Uses python3
def InsertionSert(arr):
	length = len(arr)
	for j in range(1,length):
		key = arr[j]
		i = j - 1
		while i >= 0 and arr[i] > key:
			arr[i+1] = arr[i]
			i -= 1
		arr[i+1] = key
	return arr

if __name__ == "__main__":
	arr = [5,6,8,2,3]
	result = InsertionSert(arr)
	print(result)