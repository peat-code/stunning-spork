"""
Combination sum 2
https://leetcode.com/problems/combination-sum-ii/description/

can the idx be the start of the answer

run a for loop from idx to end
    f(idx,target,listnow) 
    
    Base condition: target == 0 
    The calls are 
        1. At idx, pick idx, next call will be at f(idx+1, target-nums[idx],listnow.append(nums[idx]))
        2. Come back to idx, fix nums and target, do not pick idx, move to element idx2 with different value. 

Example: [1,1,1,2,2,3]
        pick 1 at idx = 0 , then skip till idx 3.
        In call for idx = 1, made at idx = 0, pick or not pick 1 at idx = 1, then skip till idx 3.

"""
nums = [1,1,1,2,2,3,6,8]
nums.sort()
target = 8
ans = []
def findComb(idx,target,listnow):
    if target == 0:
        ans.append(listnow.copy())
    
    for i in range(idx,len(nums)):
        if i>idx and nums[i] == nums[i-1]:   # skipping over repeated numbers
            continue
        if nums[i] > target:
            break
        
        # the calls -> take 
        listnow.append(nums[i])
        target -= nums[i]
        findComb(i+1,target,listnow)

        # fix 
        t = listnow.pop()
        target += t


findComb(0,target,[])
print(ans)