# palindrome

def palcheck(string,i,n):
    if i > n//2:
        return True
    if string[i] == string[n-i-1]:
        return  palcheck(string,i+1,n)
    else:
        return False


string = "raceecare"
n = len(string)
print(palcheck(string,0,n))