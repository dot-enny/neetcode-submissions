class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr):
            if len(arr) < 2:
                return arr

            mid = len(arr) // 2
            leftArr = arr[:mid]
            rightArr = arr[mid:]

            return merge(mergeSort(leftArr), mergeSort(rightArr))
        
        def merge(leftArr, rightArr):
            sortedArr = []
            while(len(leftArr) and len(rightArr)):
                if leftArr[0] <= rightArr[0]:
                    sortedArr.append(leftArr.pop(0))
                else:
                    sortedArr.append(rightArr.pop(0))
            return [*sortedArr, *leftArr, *rightArr]

        return mergeSort(nums)