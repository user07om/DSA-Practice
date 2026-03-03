class TwoPointers:
    def __init__(self, arr):
        self.arr = arr

    def rev_arr(self):
        left = 0
        right = len(self.arr)-1
        while left < right:
            self.arr[left], self.arr[right] = self.arr[right], self.arr[left]
            left += 1
            right -= 1

        return self.arr

    def rev_str(self):
        s = list(self.arr)
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] == " ":
                left += 1
                continue

            if s[right] == " ":
                right -= 1
                continue

            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return "".join(s)

class SlidngWin:
    def __init__(self, arr, k=None):
        self.arr = arr
        if k!=None: self.k = k

    def max_sum(self):
        max_sum = sum(self.arr[:self.k])
        curr_sum = max_sum
        for right in range(k, len(self.arr)):
            left = right-k # it remove the left most from the window.
            curr_sum += self.arr[right]
            curr_sum -= self.arr[left]
            max_sum = max(max_sum, curr_sum)

        return max_sum

    def max_vowels(self):
        vo = set("aeiou")
        curr_vo = sum(1 for x in self.arr[:k] if x in vo)
        max_vo = curr_vo
        for right in range(k, len(self.arr)):
            left = right-k
            if self.arr[right] in vo:
                curr_vo += 1
            if self.arr[left] in vo:
                curr_vo -= 1

            max_vo = max(max_vo, curr_vo)

        return max_vo

    def max_avg(self):
        curr_avg = sum(self.arr[:k])
        max_avg = curr_avg

        for right in range(k, len(self.arr)):
            left = right-k
            curr_avg += self.arr[right]
            curr_avg -= self.arr[left]
            max_avg = max(max_avg, curr_avg)

        return max_avg / k

    def long_substr(self):
        """
        Psudo Code:
            - keep the recode using hashset.
            - iterate over the string.
            - if the char is distinct.
                - curr_count += 1
            - while char in hashset 
                - till i-k.
            - add char into hashset
        """
        left = 0
        max_len = float("-inf")
        char_set = set()
        for right in range(len(self.arr)):
            while self.arr[right] in char_set:
                char_set.remove(self.arr[left])
                left += 1

            char_set.add(self.arr[right])
            max_len = max(max_len, right-left+1)

        return max_len

    def long_k_dis(self):
        """
        
        """
        max_len = float("-inf")
        left = 0
        char_set = set()
        count = 0
        for right in range(len(self.arr)):
            while count > k:
                char_set.remove(self.arr[left])
                count -= 1
                left += 1
            char_set.add(self.arr[right])
            count += 1
            max_len = max(max_len, right-left+1)

        return max_len



#TWO POINTERS EXAMPLES
arr = "omkar is" 
tp = TwoPointers(arr)
#pr1 = tp.rev_arr()
pr2 = tp.rev_str()
print(pr2)

#SLIDING WINDOW EXAMPLES
arr = "eceba"
k = 2
sw = SlidngWin(arr, k)
#pr1 = sw.max_sum()
#pr2 = sw.max_vowels()
#pr3 = sw.max_avg()
#pr4 = sw.long_substr()
pr5 = sw.long_k_dis()
print(pr5)
