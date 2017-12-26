#ifndef NLOGNSORT_SHELLSORT_H
#define NLOGNSORT_SHELLSORT_H

template<typename T>
void ShellSort(T arr[], int n){
	int h = 1;
	while (h < n/3)
	{
		h = 3 * h + 1;
	}
	while (h >= 1)
	{
		for (int i = h; i < n; i++)
		{
			T e = arr[i];
			int j;
			for (j = i; j >= h && e < arr[j - h]; j -= h)
			{
				arr[j] = arr[j - h];
			}
			arr[j] = e;
		}
		h/=3;
	}
	return;
}

#endif // !NLOGNSORT_SHELLSORT_H
