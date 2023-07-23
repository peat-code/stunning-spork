""" Recursion : 
            When a fn calls itself
            until a specified condition is met (base condition)
"""
# stack overflow
def fn():
    print(1)
    fn()

fn()