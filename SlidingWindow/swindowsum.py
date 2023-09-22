i = 0
j = 0
csum = 0
length  = -1
while j<len(nums):    
    csum += nums[j]
    j += 1
    while i<=j and csum > tofind:
        csum -= nums[i]
        i += 1
    if csum == tofind:
        length = max(length,j-i)
    
