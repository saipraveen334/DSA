class Solution {
    public int[] sortArray(int[] nums) {
        mergeSort(nums , 0 , nums.length -1 );

        return nums;
    }
        //MERGE SORT 

        //CONQUER

        void merge(int arr[] , int L , int M , int R)
        {
            int lsize = M - L + 1;
            int rsize = R - M;

            int left[] = new int[lsize];
            int right[] = new int[rsize];

            for(int i = 0 ; i < lsize ; i++)
            {
                left[i] = arr[L + i];
            }

            for(int j = 0 ; j < rsize ; j++)
            {
                right[j] = arr[M + 1 + j];
            } 

            // POINTERS

            int i = 0 ;
            int j = 0 ;
            int k = L ;

            while( i < left.length && j < right.length)
            {
                if(left[i] <= right[j])
                {
                    arr[k] = left[i];
                    i += 1;
                }
                else
                {
                    arr[k] = right[j];
                    j += 1;
                }
                k += 1;
            }

            while( i < left.length)
            {
                arr[k] = left[i];
                i += 1;
                k += 1;
            }

            while( j < right.length)
            {
                arr[k] = right[j];
                j += 1;
                k += 1;
            }
        }
 
        //DIVIDE 

        void mergeSort(int arr[] , int l , int r)
        {
            if(l >= r)
            {
                return;
            }
            int m = (r + l) / 2 ;

            mergeSort(arr, l , m) ;
            mergeSort(arr , m + 1 , r);

            merge(arr , l , m , r) ;

        }

      

        
        
    }
