#include <iostream>
using namespace std;

int main(){
	int arr[] = {51,78,32,75,95,30};
	int n = sizeof(arr)/sizeof(int);
	for(int i=1;i<n;i++){
		int current = arr[i];
		int hole = i;
		while(hole > 0 && arr[hole-1] > current){
			arr[hole] = arr[hole-1];
			hole = hole-1; 
		}
		arr[hole] = current;
	}
	for(int j=0;j<n;j++){
		cout<<arr[j]<<" ";
	}
}