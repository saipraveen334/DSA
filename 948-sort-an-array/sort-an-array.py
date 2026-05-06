class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #MERGE SORT 

        # CONQUER

        def merge(arr , m , l , r):
            leftArr = arr[l : m + 1]
            rightArr = arr[m + 1 : r + 1]
            i = 0 
            j = 0 
            k = l 

            while i < len(leftArr) and j < len(rightArr):

                if leftArr[i] < rightArr[j]:
                    arr[k] = leftArr[i]
                    i += 1
                else:
                    arr[k] = rightArr[j]
                    j += 1
                
                k += 1
            while i < len(leftArr):
                arr[k] = leftArr[i]
                i += 1
                k += 1
            while j < len(rightArr):
                arr[k] = rightArr[j]
                j += 1
                k += 1

            return arr
            




        #DIVIDE 

        def mergeSort(arr , l , r ):

            if l >= r:
                return 

            m = (l + r) // 2

            mergeSort(arr , l , m)
            mergeSort(arr , m + 1 , r)
            merge(arr , m , l , r )


        mergeSort(nums , 0 , len(nums) - 1)

        return nums