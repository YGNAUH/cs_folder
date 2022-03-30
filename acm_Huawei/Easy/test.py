def grow(n):
    print("@",n)
    if(n < 4):
        grow(n+1)
    print("f",n)
grow(1)