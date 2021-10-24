#Fibonacci Series
n = int(input("numbers: "))
def fib(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        for n in range (0, n):
            return fib(n-1) + fib(n-2)
print(fib(n), end=" ")