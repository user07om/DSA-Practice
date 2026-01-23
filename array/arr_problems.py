#ONE-----------partition array by condition..
#[even]+[odd] array (maintain the relative order)
arr = [8]

j = 0
for i in range(len(arr)):
    if (arr[i] % 2) == 0:
        arr[i], arr[j] = arr[j], arr[i]
        j += 1

print(arr, "[even] + [odd] array")


#TWO----------Find k'th largest element.
arr = [3, 2, 1, 5, 6, 4]
k = 3

largest = float("-inf")
kth_largest = float("-inf")

for i in range(len(arr)):
    if arr[i] > largest:
        kth_largest = largest
        largest = arr[i]
    elif arr[i] != largest and arr[i] > kth_largest:
        kth_largest = arr[i]

print(kth_largest)


#THREE----------Rotate Array left by k.
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3

def rev_arr(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

rev_arr(arr, 0, len(arr)-1)
rev_arr(arr, 0, k-1)
rev_arr(arr, k, len(arr)-1)
print(arr)

print(arr, k)



#THREE-----------REMOVE DUBLICATES. -- practice...
#arr = [1, 2, 3, 3, 2, 1]
#j = len(arr)-1
#val = 3
#for i in range(len(arr)-1, 0, -1):
#    if arr[i] == val:
#        arr[i], arr[j] = arr[j], arr[i]
#        j -= 1
#
#print(arr)




