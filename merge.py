def mergeSort(arr):
	if len(arr)>1:
		mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]
		mergeSort(L)
		mergeSort(R)
		i=j=k=0
		while i<len(L) and j<len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i+=1
			else:
				arr[k] = R[j]
				j+=1
			k+=1
		while i<len(L):
			arr[k]=L[i]
			i+=1
			k+=1
		while j<len(R):
			arr[k]=R[j]
			j+=1
			k+=1

# if __name__ == '__main__':
arr = [64,25,12,22,11]
print arr
mergeSort(arr)
print arr

# Explanation :-
# 1.We divide the original array into two halves until the array contains single element (divide).
# 2.Then compare the elements of arrays and store them in another empty array in ascending order (conquer).

# Time Complexity :-
# Worst Case - O(n*log n)
# Best Case - O(n*log n)
# Average Case - O(n*log n)