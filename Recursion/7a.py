# print subsequence whose sum is k

nums = [3,1,2,4,5,7]
sum = 7

def findsub(idx,listnow,sumnow):
    if idx > len(nums)-1:
        return 
    if sumnow == sum:
        print(listnow)
        return
    if sumnow > sum or idx == len(nums)-1:
        return
    
    # call 1: take el[idx] and move up
    listnow.append(nums[idx])
    sumnow += nums[idx]
    findsub(idx+1,listnow,sumnow)

    # call 2: fix array so as to not take el[idx] and move up
    temp = listnow.pop()
    sumnow -= temp
    findsub(idx+1,listnow,sumnow)

findsub(0,[],0)
