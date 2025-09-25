class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Given: 
            s string given
            vowels in string can appear both cases. (U,L)
        Task: 
            Reverse only the vowels within the string
        Approach: 
            Two Pointer: Opposite

            vowels string:
            if left in vowels, replace with right vowels until hold that position
        # """
        #okay solving three variations of same problems withing 10 minutes.
        #already know the code, understanding the limit. can i solve it.
        #first approach is two pointer, opposite ends.
        s = list(s)
        v = "aeiouAEIOU"
        left, right = 0, len(s)-1
        while left < right:

            #this for increament the left pointer till char is not vowel
            #same for right pointer as well once the both skipp the swap will happen
            #if left index is also the vowel and right then end condition meet and swap happend
            #and both pointer get increament.
            while left < right and s[left] not in v:
                left += 1
            
            while left < right and s[right] not in v:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)

    def secondApproach(s: str) -> str:
        #this second apporach with the positions of vowels
        #storing thier positions and swaping them, by left and right pointers.
        #uses extra space but gives good time means effecient. but not friendly
        s = list(s)
        v = "aeiouAEIOU"
        p = [i for i, c in enumerate(s) if c in v]
        left, right = 0, len(p)-1
        while left < right:
            s[p[left]], s[p[right]] = s[p[right]], s[p[left]]
            left += 1
            right -= 1
        
        return ''.join(s)


    def thirdApproach(s: str) -> str
        s = list(s)
        v = "aeiouAEIOU"
        p = [c for c in s if c in v]
        output = []
        for c in s:
            if c in v:
                output += p.pop()
            else:
                output += c
        return ''.join(output)
