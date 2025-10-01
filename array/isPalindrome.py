class Solution:
    def isPali(self, phrase: str) -> bool:
        """
        it's two pointer approach - left, right
        """
        left, right = 0, len(phrase)-1

        while left < right:
            #increament left if it has not the alphanumeric char.
            while left < right and not phrase[left].isalnum():
                left += 1

            #increament right if it has not the alphanumeric char.
            while left < right and not phrase[right].isalnum():
                right -= 1

            if phrase[left] != phrase[right]:
                return False

            left += 1
            right -= 1

        return True


sol = Solution()
print(sol.isPali("race -9032 car"))
