# print from n to 1
# print from 1 to n

def printrev(n):
    if n == 0:
        return
    print(n)
    printrev(n-1)
def printto(n):
    if n == 0:
        return
    printto(n-1)
    print(n)

printrev(30)
printto(20)