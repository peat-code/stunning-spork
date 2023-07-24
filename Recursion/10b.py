"""
Subset Sum
arr[] = {2, 3} 
Output: 0 2 3 5

Without using extra space 
(listnow)


"""
nums = [3,1,6]
hset =set()
def subsum(idx,sumnow):
    # two calls, take and not take
    if idx == len(nums):
        hset.add(sumnow)
        return
    subsum(idx+1,sumnow)

    subsum(idx+1,sumnow + nums[idx])

subsum(0,0)
print(hset)
