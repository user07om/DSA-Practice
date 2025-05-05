
def lr_arr_op(arr: list) -> list:
    temp = arr[0]
    for i in range(len(arr)-1):
        arr[i-1] = arr[i]
    arr[len(arr)-1] = temp
    return arr

print(lr_arr_op([1,2,3,4,5]))
            

