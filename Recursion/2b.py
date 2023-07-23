# backtrack


def fn(i,n):
    if i < 1:
        return 
    fn(i-1,n)
    print(i)

def fn2(i,n):
    if i > n:
        return
    fn2(i+1,n)
    print(i)

# fn(5,5)
fn2(0,5)