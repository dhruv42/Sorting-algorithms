arr = [64,25,12,22,11]
print arr
for i in range(1,len(arr)):
	curr = arr[i]
	hole = i
	while(hole>0 and arr[hole-1]>curr):
		arr[hole] = arr[hole-1]
		hole-=1
	arr[hole] = curr
print arr


# Explanation :-
# 1.Start with the 2nd element of the array.
# 2. compare it with the elements before it.
# 3.Swap if the curr element is smaller than the prev element till it reaches it's proper position.


# Time complexity :-
# Best - O(n)
# Average - O(n*2)
# Worst - O(n*2) 