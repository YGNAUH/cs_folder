def lcm(a: int, b: int):
    def gcd(a: int, b: int):
        if b == 0:
            return a
        else:
            print(b,a%b)
            return gcd(b, a % b)
        
    return int((a * b) / gcd(a, b))

a, b = map(int, input().split())
print(lcm(a, b))