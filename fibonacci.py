fib1 = 0
fib2 = 1
n=int(input("Enter the limit:"))
for i in range(n):
    print(fib1)
    fib=fib1+fib2
    fib1=fib2
    fib2=fib

