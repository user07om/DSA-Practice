
def hammingDist(x, y) -> int: #the XOR not support to string!
    # the bin() convert it to binary format.
    return bin(x ^ y).count('1') #if the char differe then it denote as 1. a XOR b


def hammingDistance(s1, s2):
    return sum((x ^ y) for x, y in zip(s1, s2))
    

print(hammingDistance(1, 1))
