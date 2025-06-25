class Solution:
    def mySqrt(self, x: int) -> int:
        """
        1. we use the BS, assign left, right as 0 and max length is x
        2. then we get the sq of each number till iteration stops.
        3. aa
        """
        left, right = x, 
        res = 0
        while left <= right:   #0<1
            mid = int((left+right)//2)  #1   #right - 3
            sq = mid**2  #1
            if sq <= x: #1<=4 wrong
                left = mid+1  #1+1
                res = mid
            else:
                right = mid-1   #3

        return res
    
    print(mySqrt(8))


            

