class InsertVal:
    """
    insert element at specific idx. rear, tail and user-input.
    """
    def __init__(self, arr):
        self.arr = arr

    def insert_first(self, val):
        """
        make extra space in array, and iterate in reverse order
        assign second last element to last element, this way - it
        shipts all element to rigth side, then assign arr[0] given value.
        """
        self.arr.append(0) # adding extra space.
        n = len(self.arr)
        for i in range(n-1, 0, -1):
            self.arr[i] = self.arr[i-1]

        self.arr[0] = val

    # we don't do the insert at end, cause we can simpli accept this using arr.append()

    def insert_input(self, val, idx):
        """
        we follow the same pricince that we use for the insert at first, only small
        change in we stop the iteration at idx or user give.
        """
        self.arr.append(0)
        n = len(self.arr)
        for i in range(n-1, idx-1, -1):
            self.arr[i] = arr[i-1]

        self.arr[idx-1] = val

    def insert_variable_way(self, val, idx):
        """
        this method uses the extra variable, it's store the new ele to temp variable. 
        it start the loop from idx..to..n, then it's store the curr element in curr_val
        assign the temp to that position, and store the curr_val to temp variable. it's loop. till end.
        """
        self.arr.append(0) 
        n = len(self.arr)
        temp = val
        for i in range(idx-1, n):
            curr_val = self.arr[i]
            self.arr[i] = temp
            temp = curr_val


if __name__ == __main__:

    #ELEMENT INSERTION AT GIVEN INDEX INPUT AND VALUE.
    arr = [1, 2, 3, 4]
    insert = InsertVal(arr)
    #opr = insert.insert_first(9)
    #opr = insert.insert_input(9, 2)
    #opr = insert.insert_variable_way(9, 3)
    print(arr)

    #MOVE ZEROS TO END MULTIPLE VARIATIONS
    arr = [0, 1, 0, 0, 2, 0]
