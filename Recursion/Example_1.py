# Q. Find factorial of any number n.

def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
    
print("factorial of number n:", fact(5))