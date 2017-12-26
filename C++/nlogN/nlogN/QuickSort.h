#ifndef NLOGNSORT_QUICKSORT_H
#define	NLOGNSORT_QUICKSORT_H

#include <iostream>
#include <algorithm>
#include "InsertSort.h"

using namespace std;

template<typename T>
int __Parttion(T arr[], int l, int r){
	T v = arr[l];
	int j = l;
	for (int i = l + 1; i <= r; i++)
	{
		if (arr[i] < v)
		{
			swap(arr[j + 1], arr[i]);
			j++;
		}
	}
	swap(arr[l], arr[j]);
	return j;
}
template<typename T>
void __QuickSort(T arr, int l, int r){
	if (l >= r){
		return;
	}
	int p = __Parttion(arr, l, r);
	__QuickSort(arr, l, p);
	__QuickSort(arr, p+1, r);
}
template<typename T>
void QuickSort(T arr[], int n)
{
	__QuickSort(arr, 0, n - 1);
	return;
}
#endif // !NLOGNSORT_QUICKSORT_H
