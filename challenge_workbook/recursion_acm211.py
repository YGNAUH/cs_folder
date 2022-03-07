def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

memo = {}
def fibversion1(n):
    if n <= 1:
        return n
    else:
        return fibversion1(n-1) + fibversion1(n-2)

def fib(n):
    if n <= 1:
        return n
    else:
        if n in memo:
            return memo[n]
        else:
            memo[n] = fib(n-1) + fib(n-2)
            print(memo)
            return memo[n]

while(1):
    try:
        n = int(input())
        fv1 = fibversion1(n)
        f = fib(n)
        print(f, fv1)
    except:
        break