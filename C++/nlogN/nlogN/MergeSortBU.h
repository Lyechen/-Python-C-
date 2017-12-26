#ifndef NLOGNSORT_MERGESORTBU_H
#define	NLOGNSORT_MERGESORTBU_H

#include "InsertSort.h"

template<typename T>
void MergeSortBU(T arr[], int n)
{
	for (int sz = 1; sz <= n; sz += sz)
	{
		//��[i...i+sz-1]��[i+sz....i+sz+sz-1]��һ�ι鲢
		for (int i = 0; i + sz < n; i+= sz + sz)
		{
			if (arr[i + sz - 1] > arr[i + sz])
			{
				__Merge(arr, i, i + sz - 1, min(i + sz + sz - 1, n-1));
			}
		}
	}
}
#endif // !NLOGNSORT_MERGESORTBU_H
