def fib(n):
    print 1
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print fib(5)
