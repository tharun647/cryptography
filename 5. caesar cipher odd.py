def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
for a in range(26):
    if gcd(a, 26) == 1:
        print(f"a = {a} is allowed")
    else:
        print(f"a = {a} is not allowed")
print()
        
