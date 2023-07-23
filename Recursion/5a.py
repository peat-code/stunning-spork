# multiple recursion calls
# measuring difference between w and w/o memo on fibonacci.
import time


# fibonacci number
def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)
# each calls two functions 
# TC = 2 power n



# fib with memoization
dp = [-1] * 100
def fibmemo(n):
    if dp[n] != -1:
        return dp[n]
    if n < 2:
        dp[n] = 1
        return dp[n]
    dp[n] = fibmemo(n-1) + fibmemo(n-2)
    return dp[n]


start = time.time()
print(fib(48))
end = time.time()
print(end - start)

start = time.time()
print(fibmemo(48))
end = time.time()
print(end - start)

