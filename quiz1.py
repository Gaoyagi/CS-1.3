def complete_sum(n):
    sum = n
    for x in range(n):
        sum+=x
    return sum

# def complete_sum_recurse(n, sum=0):
#     if n!=0:
#         sum+=n
#         n-=1
#         return complete_sum_recurse(n, sum)
#     return sum


#pseudo code for q6:
def binary_search(list, number, left, right):
    if current number hasnt been found:
        find mid point within the left right point
        if midpoint number larger than target number
            make left right boundires the lower half of the problem size
            recurse
        else mid point number less than target number
            make elft right boundires the upp half of the problem size
            recurse