class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        count = 0
        
        for i in range(len(flowerbed)):
            if count == n:
                return True
            if i == 0:
                if len(flowerbed) == 1:
                    if n == 0 and flowerbed[i] == 1:
                        return False
                    if n == 0 and flowerbed[i] == 0:
                        return True
                elif flowerbed[i] != 1 and flowerbed[i+1] != 1:
                    flowerbed[i] = 1
                    count += 1
            if i == len(flowerbed) - 1:
                if flowerbed[i-1] != 1 and flowerbed[i] != 1:
                    flowerbed[i] = 1
                    count += 1
            else:
                if flowerbed[i] != 1 and flowerbed[i-1] != 1 and flowerbed[i+1] != 1:
                    flowerbed[i] = 1
                    count += 1

        return (count >= n)