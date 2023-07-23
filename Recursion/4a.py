# reverse array using recursion

def revarr(nums,i,j):
    if i >j:
        return
    nums[i],nums[j] = nums[j] ,nums[i]
    revarr(nums,i+1,j-1)

# reducing parameters
def revarr2(nums,i):
    if i > len(nums)//2:
        return
    nums[i],nums[len(nums)-i-1] = nums[len(nums)-i-1] ,nums[i]
    revarr2(nums,i+1)
nums = [1,2,3,4,5,6,7,8,9]
# nums = [0,1,2]
print(nums)
revarr2(nums,0)
print(nums)