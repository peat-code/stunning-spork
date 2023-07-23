# sum of n numbers recursion

# fs1 = (10,0) -> (9,10) -> (8,19) -> (7,27) -> (6,33)
def fs(n,sum):
    if n <1:
        return sum
    return fs(n-1,sum+n)
# print(fs(10,0))


# fs2 = (10) -> 10 + (9) -> 19 + (8) -> 27 +(7)
def fs2(n):
    if n ==0:
        return 0
    return n +fs2(n-1)
# print(fs2(10))

# n factorial 

# parameters
def fc(n,fact):
    if n == 0:
        return fact
    return fc(n-1,fact * n )
print(fc(4,1))

def fc2(n):
    if n == 0:
        return 1
    return fc2(n-1) * n
print(fc2(4))