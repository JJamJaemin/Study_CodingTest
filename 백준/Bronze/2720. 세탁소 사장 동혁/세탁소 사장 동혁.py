# 25센트 10센트 5센트 1센트
T = int(input())
for i in range(T):
    quarter = 0
    dime = 0
    nickel = 0
    penny = 0
    n = int(input())
    if n >= 25:
        quarter = n // 25
        n = n % 25
    if n >= 10:
        dime = n // 10
        n = n % 10
    if n >= 5:
        nickel = n // 5
        n = n % 5
    penny = n // 1
    n = n - penny
    print(quarter, dime, nickel, penny)

