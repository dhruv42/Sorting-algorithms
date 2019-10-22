#include <iostream>
#include <climits>
// #include <chrono>
using namespace std;
// using namespace std::chrono; 
int main(){
	int arr[] = {51,78,32,75,95,30};
	int n = sizeof(arr)/sizeof(int);
	// auto start = high_resolution_clock::now(); 
	for(int j=0;j<n-1;j++){
		for(int i = 0;i<n-j-1;i++){
			if(arr[i]>arr[i+1]){
				int temp = arr[i];
				arr[i] = arr[i+1];
				arr[i+1] = temp;
			}
		}	
	}
	// auto stop = high_resolution_clock::now(); 
	// auto duration = duration_cast<microseconds>(stop - start); 
	for(int k=0;k<n;k++){
		cout<<arr[k]<<" ";
	}
	// cout<<"\n"<<duration.count()<<"ms\n";
}