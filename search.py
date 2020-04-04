#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    print(index)
    if index != len(array): 
        if array[index] == item:
            return index
        index+=1
        print(index)
        return linear_search_recursive(array, item, index)
    return None


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    curr = int((len(array)/2))
    while array[curr] != item:
        if array[curr] < item:
            curr += int((len(array)-curr)/2)
        elif array[curr] > item:
            curr = int(curr/2)   

        if curr == 0 or curr == len(array)-1:
            if array[curr] != item:
                return None
    return curr

def binary_search_recursive(array, item, left=None, right=None):
    #check for first time running the function
    if left == None and right == None:
        left = 0
        right = len(array)-1
    #gets the middle index
    curr = int((right-left)/2)
    if curr == 0:       #if the division gives a 0 then make it the difference between
        curr = right-left
    curr = left + curr
    #make sure the indexes dont overlap, if they overlap it means the item isnt there
    if right<left:
        return None
    #check to see  if the item is found, if not recurse
    print(right)
    print(left)
    print(curr)
    if array[curr] != item:
        if array[curr] < item:
            left = curr+1
            return binary_search_recursive(array, item, left, right)
        elif array[curr] > item:
            right = curr-1
            return binary_search_recursive(array, item, left, right)
    return curr



names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
# print(binary_search(names, 'Nobody'))

print(binary_search(names, 'Alex'))