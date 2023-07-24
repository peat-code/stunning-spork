"""
Subset Sum
arr[] = {2, 3} 
Output: 0 2 3 5


"""
nums = [3,1,6]
hset =set()
def subsum(idx,listnow):
    # two calls, take and not take
    if idx == len(nums):
        b = sum(listnow)
        hset.add(b)
        return
    subsum(idx+1,listnow)

    listnow.append(nums[idx])
    subsum(idx+1,listnow)
    listnow.pop()

subsum(0,[])
print(hset)
