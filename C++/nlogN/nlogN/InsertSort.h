#ifndef NLOGNSORT_INSERTSORT_H
#define NLOGNSORT_INSERTSORT_H
template<typename T>
void InsertSort(T arr[], int n){
	for (int i = 1; i < n; i++)
	{
		T e = arr[i];
		int j;
		for (j = i; j > 0 && e < arr[j - 1]; j--)
		{
			arr[j] = arr[j - 1];
		}
		arr[j] = e;
	}
	return;
}
template<typename T>
void CustomInsertSort(T arr[], int l, int r){
	for (int i = l + 1; i <= r; i++)
	{
		T e = arr[i];
		int j;
		for (j = i; j > l && e < arr[j - 1]; j--)
		{
			arr[j] = arr[j - 1];
		}
		arr[j] = e;
	}
	return;
}
#endif // !NLOGNSORT_INSERTSORT_H
