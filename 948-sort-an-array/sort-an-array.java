class Solution {

    public int[] sortArray(int[] nums) {
        mergeSort(nums, 0, nums.length - 1);
        return nums;
    }

    void merge(int arr[], int L, int M, int R) {

        int lsize = M - L + 1;
        int rsize = R - M;

        int[] left = new int[lsize];
        int[] right = new int[rsize];

        for (int i = 0; i < lsize; i++) {
            left[i] = arr[L + i];
        }

        for (int j = 0; j < rsize; j++) {
            right[j] = arr[M + 1 + j];
        }

        int i = 0, j = 0, k = L;

        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                arr[k] = left[i];
                i++;
            } else {
                arr[k] = right[j];
                j++;
            }
            k++;
        }

        while (i < left.length) {
            arr[k] = left[i];
            i++;
            k++;
        }

        while (j < right.length) {
            arr[k] = right[j];
            j++;
            k++;
        }
    }

    void mergeSort(int arr[], int l, int r) {

        if (l >= r) return;

        int m = (l + r) / 2;

        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);

        merge(arr, l, m, r);
    }
}