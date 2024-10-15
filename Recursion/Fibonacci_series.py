# Q. Fibonacci Series

def fibo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibo(n-1)+fibo(n-2) # Time Complexity: O(2^n)
print ("Fibonacci Series of: ", fibo(10))