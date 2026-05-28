from collections import Counter
def problem(arr, k):
    count = Counter(arr)

    freq = [[] for _ in range(len(arr)+1)]

    for key, val in count.items():
        freq[val].append(key)

    res = []
    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


print(problem([1, 2, 2, 3, 3, 3], 2))
    
#-------------------------practice lambda functions and it's variations:
#sorted with lambda as key passing.
#most usefull functions for lamda to be used.
"""
sort()
sorted()
map()
reduce()
filter()
categories: dictionary, heaps, constome comparisons
"""
#basic lambda usage: just store it in vairable and print it or directly pring it.
square = lambda x: x**2
print(square(4))
