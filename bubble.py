arr = [64,25,12,22,11]
print arr
for i in range(len(arr)):
	for j in range(len(arr)-i-1):
		if(arr[j+1]<arr[j]):
			arr[j],arr[j+1] = arr[j+1],arr[j]
print arr


# Explanation :-
# 1.Starting with the first element, compare the current element with next element
# 2.if the current element is greater than the next element then swap then
# 3.if current element is less than the next element, then move to next element and repeat step 1


# Time complexity :-
# Best - O(n)
# Average - O(n*2)
# Worst - O(n*2)