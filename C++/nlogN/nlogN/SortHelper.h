#ifndef NLOGNSORT_SORTHELPER_H
#define	NLOGNSORT_SORTHELPER_H

#include <iostream>
#include <algorithm>
#include <ctime>
#include <string>
#include <cassert>

using namespace std;
namespace SortHelper{
	template<typename T>
	bool isSort(T arr[], int n){
		/*�ж��Ƿ���һ������������ϵ�����*/
		for (int i = 0; i < n - 1; i++)
			if (arr[i] > arr[i + 1])
				return false;
		return true;
	}
	int* generateRandomArray(int n, int rangel, int rangeR){
		/*����һ������Ϊn��������飬ֵ�÷�Χ��Ϊ[rangel, rangeR]����*/
		int* arr = new int[n];
		srand(time(NULL));
		for (int i = 0; i < n; i++)
		{
			arr[i] = rand() % (rangeR - rangel + 1) + rangel;
		}
		return arr;
	}
	template<typename T>
	T* copyArray(T a[], int n){
		T* arr = new int[n];
		for (int i = 0; i < n; i++)
		{
			arr[i] = a[i];
		}
		return arr;
	}
	template<typename T>
	void testSort(const string &sortName, void(*sort)(T[], int), T arr[], int n){
		clock_t startTime = clock();
		sort(arr, n);
		clock_t endTime = clock();
		assert(isSort(arr, n));
		cout << sortName << ": " << double((endTime - startTime)) / CLOCKS_PER_SEC << "s" << endl;
		return;
	}
	template<typename T>
	void printArray(T arr, int n){
		for (int i = 0; i < n; i++)
		{
			cout << arr[i] << " ";
		}
		cout << endl;
	}
}
#endif // !NLOGNSORT_SORTHELPER_H
