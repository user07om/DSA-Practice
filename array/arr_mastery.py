class Basics:
    def two_sum(self, arr, target) -> list[int]:
        #unsorted array so we use the dictionary here.
        seen = {}
        for i in range(len(arr)):
            comp = target - arr[i]
            if comp in seen:
                return [i, seen[comp]]
            
            seen[arr[i]] = i

        return [0, 0]

    def best_time_to_buy_and_sell(self, arr) -> int:
        profit = 0
        buy = float("inf") #max infinite number/integer.
        for i in range(len(arr)):
            buy = min(buy, arr[i])
            profit = max(profit, arr[i] - buy)

        return profit

    def contains_dublicates(self, arr) -> bool:
        seen = set()
        for i in range(len(arr)):
            if arr[i] in seen:
                return True
            seen.add(arr[i])

        return False

    def max_subarray(self, arr) -> int:
        ...

    def range_sum_query(self, arr, l, r) -> int:
        pre = [0]*(len(arr)+1)
        pre[1] = arr[0]
        for i in range(1, len(arr)):
            pre[i+1] = pre[i] + arr[i]

        return pre[r+1] - pre[l], pre 

    def subarr_sum_eq_k(self, arr, k):
        #prefix array creation
        pre = [0]*len(arr)
        pre[0] = arr[0]
        for i in range(1, len(arr)):
            pre[i] = pre[i-1] + arr[i]

        res = 0
        pre_map = { 0: 1 }
        for i in range(len(pre)):
            val = pre[i] - k
            if val in pre_map:
                res += pre_map[val]

            if pre[i] not in pre_map:
                pre_map[pre[i]] = 0
            pre_map[pre[i]] += 1

        return res 




easy = Basics()
pr1 = easy.range_sum_query([1, 2, 3, 4], 1, 3)
print("range sum query problem: ", pr1)


pr2 = easy.subarr_sum_eq_k([1, 1, 1], 2)
print(pr2)
