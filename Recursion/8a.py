# combination sum
# [2,3,6,7] target = 7
# {2,2,3} {7}

"""
for every index, we pick it 0 to j times, such that sum <= target

for loop for no of times, 
function call (idx,sumNow,listNow[])

"""

nums = [2,3,6,7]
target = 7
ans = []
def combsum(idx,need,listnow):
    if idx==len(nums)-1:
        if need == 0:
            ans.append(listnow.copy())
        return 
    if need < 0:
        return

    # stay at current to add again or move up.
    listnow.append(nums[idx])
    need -= nums[idx]
    combsum(idx,need,listnow)
    need += nums[idx]
    listnow.pop()
    combsum(idx+1,need,listnow)

combsum(0,target,[])
print(ans)
