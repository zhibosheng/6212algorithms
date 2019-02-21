#Uses python3
def  BinarySearch(arr, val, left,right):
	if right < left:
		return -1
	mid = (left + right)//2
	if mid > val:
		return BinarySearch(arr,val,left,mid-1)
	elif mid < val:
		return BinarySearch(arr,val,mid+1,right)
	else:
		return mid

if __name__ == "__main__":
	arr = [1,2,5,9,10,12,16,20]
	result = BinarySearch(arr,5,arr[0],arr[-1])
	print(result)