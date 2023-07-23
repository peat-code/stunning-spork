# print all subsequences  
# subsequence -> contigous or not , must follow order
"""
[3,1,2] -> [empty],[3],[1],[2],[3,1],[3,2],[1,2],[3,1,2]
"""

# take or not take
"""
base case is when you go out of index

the calls are:  append the element at curr idx and call self on updated list and next index
                pop the element appended and call self on list and next index


"""
# TC (2 power n) times n
# two calls per idx times print n elements

# Stack space is n , we go n deep, print, come back and go again.


nums = [3,1,2,7]
n = len(nums)

# take and then not take  = 3 -> 2 -> 1 -> empty
def subs(idx,listnow):
    if idx >= n:
        print(listnow)
        return 
    listnow.append(nums[idx])
    subs(idx+1,listnow)
    # subs will go and come back 
    listnow.pop()
    subs(idx+1,listnow)
# subs(0,[])

# not take and then take =  empty -> 1 -> 2 -> 3
def subs2(idx,listnow):
    if idx >= n:
        print(listnow)
        return 
    subs2(idx+1,listnow)
    listnow.append(nums[idx])
    subs2(idx+1,listnow)
    # subs will go and come back 
    listnow.pop()
subs2(0,[])
    