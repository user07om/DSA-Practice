#CREATE 
x = [
        [5,2,3],
        [4,1,6],
        [7,8,9]
    ]
#ACCESS
r = 0; c = 0
def access(r, c):
    print(x[r][c])
    print(x[1][1])
    print(x[2][2])

#access(r, c)


#ROWS AND COLUMNS
#ROWS VISE TRAVERSLA
#COLUMNS VISE TRAVERSAL
def rowscoln():
    print("rows only: ")
    #for r in x:
        #print(r)

    print("columns only: ")
    i = 0
    while i < len(x):
        j = 0
        while j < len(x[0]):
            print(x[j][i], end=" ")
            j += 1
        print()
        i += 1

#rowscoln()


#SUM ALL ELEMENTS
res = 0
for r in x:
    res += sum(r)

#print(res)


#FIND MAXIMUM 
#FIND MINIMUM --- just change the min to max!
def findMin(x: list[list]) -> int:
    res = float("inf")
    for i in range(len(x)):
        for j in range(len(r)):
            res = min(res, x[i][j])
    
    return res

#print(findMin(x))


#MAIN DIAGNOL
for i in range(len(x)):
    #print(x[i][i])
    print(None)
#SECONDARY DIAGNOL
n = len(x)
for i in range(len(x)):
    #print(x[i][n-1-i])
    ...
#TRANSPOSE
xx = [
    [1,2,3,4],
    [5,6,7,8]
]

i = 0
while i < len(xx):
    j = 0
    while j < len(xx[0]):
        print(xx[i][j], end=" ")
        j += 1
    print()
    i += 1

import numpy as np
matrix = np.array(xx)
print(matrix.T)
print("----------------------")


s = [row for row in zip(*xx)]
print(s)

arr1 = [4, 5]
arr2 = [6, 7]
for i in zip(arr1, arr2):
    print(i)

#CREATE EMPTY MATRIX
print("--------------------------------")
r = 3
c = 2

s = [[0]*c for _ in range(r)]
print(s)

#FILL MATRIX
ele = 0
for i in range(len(s)):
    for j in range(len(s[i])):
        s[i][j] = ele
        ele += 1

#print(s)


#MODIFY EVEERY ELEMENT
#REVERSE EVERY ROW
for r in s:
    r.reverse()
#print(s)

#REVERSE EVERY COLUMN
print(xx)
row = len(xx)
col = len(xx[0])

for c in range(col):
    top = 0
    bottom = row-1
    while top < bottom:
        xx[top][c], xx[bottom][c] = xx[bottom][c], xx[top][c] 

        top += 1
        bottom -= 1

print(xx)


#FOUR DIRECTION
#VALID NEIGHBOR

