#include <iostream>
#include <climits>
// #include <chrono>
using namespace std;
// using namespace std::chrono;
int main() {
	// auto start = high_resolution_clock::now();
	int arr[] = {51,78,32,75,95,30};
	int n = sizeof(arr)/sizeof(int);
	for (int i = 0; i < n-1; i++) {
		int iMin = i;
		for (int j = i+1; j < n; j++){
			if(arr[j] < arr[iMin]){
				iMin = j;
			}
		}
		int temp = arr[i];
		arr[i] = arr[iMin];
		arr[iMin] = temp;
	}
	// auto stop = high_resolution_clock::now(); 
	// auto duration = duration_cast<microseconds>(stop - start); 
	for (int k=0;k<n;k++){
		cout<<arr[k]<<" ";
	}
	// cout<<"\n"<<duration.count()<<"ms\n";
}