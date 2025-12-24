from typing import List

class InsertionSorting:
    def problem(arr: List[int]) -> List[int]:
        for i in range(1, len(arr)):   # interate from 1 to len of arr 
            key = arr[i]               # assign the value of i idx to key variable
            j = i-1                    # assign the previeus idx to j, for comparison
            while j>=0 and arr[j]>key:  # while loop if j is greater and previeus val is greater than key.
                arr[j+1] = arr[j]      # if then assign the privous val to it's next idx.
                j -= 1                 # and decreament the j by one, this while loot true till pre is less.

            arr[j+1] = key             # reposition the again, for valid iteration.

        return arr


Sol = InsertionSorting
print(Sol.problem([2, 3, 1]))


