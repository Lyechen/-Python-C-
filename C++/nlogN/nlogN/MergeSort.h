#ifndef NLOGNSORT_MERGESORT_H
#define	NLOGNSORT_MERGESORT_H

#include "InsertSort.h"
template<typename T>
void __Merge(T arr[], int l, int mid, int r){
	T* aux = new T[r - l + 1];
	for (int i = l; i <= r; i++){
		aux[i - l] = arr[i];
	}
	int i = l, j = mid + 1;
	for (int k = l; k <= r; k++){
		if (i > mid){
			arr[k] = aux[j - l];
			j++;
		}
		else if (j > r){
			arr[k] = aux[i - l];
			i++;
		}
		else if(aux[i - l] > aux[j - l]){
			arr[k] = aux[j - l];
			j++;
		}
		else{
			arr[k] = aux[i - l];
			i++;
		}
	}
	delete[] aux;
}
template<typename T>
void __MergeSort(T arr[], int l, int r){
	/*if (l >= r){
		return;
	}*/
	if (r - l <= 15){
		CustomInsertSort(arr, l, r);
		return;
	}
	int mid = (l + r) / 2;
	__MergeSort(arr, l, mid);
	__MergeSort(arr, mid + 1, r);
	if (arr[mid] > arr[mid+1])
		__Merge(arr, l, mid, r);
}
template<typename T>
void MergeSort(T arr[], int n){
	/*自顶向上的归并排序*/
	__MergeSort(arr, 0, n - 1);
}

#endif // !NLOGNSORT_MERGESORT_H
