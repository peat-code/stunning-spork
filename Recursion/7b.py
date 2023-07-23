# print any subsquence 
# change the calls to return boolean 
# check on boolean
# no global flags

nums = [3,1,2,4,5,7]
sum = 7

def findsub(idx,listnow,sumnow):
    if idx > len(nums)-1:
        return False
    if sumnow == sum:
        print(listnow)
        return True
    if sumnow > sum or idx == len(nums)-1:
        return False
    
    # call 1: take el[idx] and move up
    listnow.append(nums[idx])
    sumnow += nums[idx]
    if findsub(idx+1,listnow,sumnow) == True:
        return True

    # call 2: fix array so as to not take el[idx] and move up
    temp = listnow.pop()
    sumnow -= temp
    if findsub(idx+1,listnow,sumnow) == True:
        return True

findsub(0,[],0)
