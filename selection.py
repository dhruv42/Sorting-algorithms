arr = [64,25,12,22,11]
print arr
for i in range(len(arr)):
	minimum = i
	for j in range(i+1, len(arr)):
		if(arr[j]<arr[minimum]):
			minimum = j
	arr[i], arr[minimum] = arr[minimum], arr[i]
print arr

# Explanation :-
# 1.Starting from the first element, we search the smallest element in the array, and replace it with the element in the first position.
# 2.We then move on to the second position, and look for smallest element present in the subarray, starting from index 1, till the last index.
# 3.We replace the element at the second position in the original array, or we can say at the first position in the subarray, with the second smallest element.
# 4.This is repeated, until the array is completely sorted.

# Time complexity of sorting algorithm,
# Best - O(n*2)
# Average - O(n*2)
# Worst - O(n*2)