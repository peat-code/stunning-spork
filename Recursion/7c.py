# print number of subsquences
# return 1 if condition satisfied
# return 0 if not
# store 1st as x , and store 2nd as y
# return x + y + .....

# multiple recursion calls 
# use for loop

nums = [3,1,2,4,5,7]
sum = 7

def findsub(idx,listnow,sumnow):
    if idx > len(nums)-1:
        return 0
    if sumnow == sum:
        # print(listnow)
        return 1
    if sumnow > sum or idx == len(nums)-1:
        return 0
    
    # call 1: take el[idx] and move up
    listnow.append(nums[idx])
    sumnow += nums[idx]
    x = findsub(idx+1,listnow,sumnow) 
    
    # call 2: fix array so as to not take el[idx] and move up
    temp = listnow.pop()
    sumnow -= temp
    y = findsub(idx+1,listnow,sumnow)
    return x + y

print(findsub(0,[],0))