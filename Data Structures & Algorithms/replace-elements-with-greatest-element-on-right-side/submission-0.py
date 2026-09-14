class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(len(arr)):

            greatest = 0

            for j in range(len(arr)):
                if arr[j] > greatest and not (j <= i):
                    greatest = arr[j]

            arr[i] = greatest
            greatest = 0

        arr[len(arr) - 1] = -1
        
        return arr