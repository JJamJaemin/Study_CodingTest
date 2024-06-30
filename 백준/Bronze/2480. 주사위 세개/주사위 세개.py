a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a == b and b == c:
    answer = 10000 + a * 1000
elif a == b or a == c:
    answer = 1000 + a * 100
elif b == c:
    answer = 1000 + b * 100
else:
    answer = max(a, b, c) * 100

print(answer)
