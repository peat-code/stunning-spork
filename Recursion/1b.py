""" Recursion : 
            When a fn calls itself
            until a specified condition is met (base condition)
"""
# base condition
def fn(n):
    if n ==1:
        return
    print(n)
    fn(n-1)

fn(7)