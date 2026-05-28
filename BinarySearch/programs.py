class EASY:
    """
    binary search template. low, high and mid - avoid infinite loop.
    1. binary search program.
    2. search insert position
    3. first bad version
    4. sqrt(x)
    5. valid perfect square
    """
    def __init__(self, arr=None):
        self.arr = arr

    def binary_search(self, target):
        start, end = 0, len(self.arr)-1
        while start <= end:
            mid = start + (end - start) // 2
            if self.arr[mid] == target:
                return mid
            elif self.arr[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return -1

    def search_ins_pos(self, target):
        start, end = 0, len(self.arr)-1
        while start <= end:
            mid = start + (end - start) // 2
            if self.arr[mid] == target:
                return mid
            elif self.arr[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return start



    def first_bad_ver(self):
        start, end = 1, n-1
        res = 0
        #while start <= end:
            #mid = start + (end - start) // 2
        # it requires the extra function for checking is server down or not
        # which returns the boolian value.
            

    def sqrt(self, x):
        if x in [1, 2, 3]:
            return 1

        res = 0

        start, end = 0, x//2
        while start <= end:
            mid = start + (end - start) // 2
            sqrt = mid ** 2
            if sqrt > x:
                end = mid - 1
            elif sqrt < x:
                res = mid
                start = mid + 1
            else:
                return mid

        return res

    def valid_perf_sqr(self, x):
        start = 0
        end = x if x <= 1 else x//2
        while start <= end:
            mid = start + (end-start)//2
            sqr = mid*mid
            if sqr == x:
                return True
            elif sqr > x:
                end = mid - 1
            elif sqr < x:
                start = mid + 1

        return False
        
    

if __name__ == "__main__":
    easy = EASY([1, 3, 5, 6]) #easy binary search patterns.
    print("binary search algorithm: ", easy.binary_search(5))
    print("search insertion position: ", easy.search_ins_pos(8))
    print("sqrt of x number: ", easy.sqrt(8))
    print("perfect sqr (bool value): ", easy.valid_perf_sqr(14))

    medium = MEDIUM() #medium binary search patterns

