#include<iostream>
#include<string>
#include "MergeSort.h"
#include "SortHelper.h"
#include "ShellSort.h"
#include "InsertSort.h"
#include "MergeSortBU.h"
#include "QuickSort.h"

using namespace std;

int main(){
	int n = 10000000;
	int* arr = SortHelper::generateRandomArray(n, 1, n);
	int* arr1 = SortHelper::copyArray(arr, n);
	int* arr2 = SortHelper::copyArray(arr, n);
	int* arr3 = SortHelper::copyArray(arr, n);
	int* arr4 = SortHelper::copyArray(arr, n);
	SortHelper::testSort("MergeSort", MergeSort, arr, n);
	SortHelper::testSort("ShellSort", ShellSort, arr1, n);
	//SortHelper::testSort("InsertSort", InsertSort, arr2, n);
	SortHelper::testSort("MergeSortBU", MergeSortBU, arr3, n);
	SortHelper::testSort("QuickSort", QuickSort, arr4, n);
	delete[] arr;
	delete[] arr1;
	delete[] arr2;
	delete[] arr3;
	/*int arr4[10] = { 0, 9, 8, 7, 6, 5, 4, 3, 2, 1 };
	MergeSortBU(arr4, 10);
	SortHelper::printArray(arr4, 10);*/
	system("pause");
	return 0;
}