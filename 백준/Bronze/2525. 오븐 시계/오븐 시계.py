a,b = input().split()
c = input()
a= int(a)
b= int(b)
c= int(c)
if b+c <= 59:
    b = b+c
elif b+c >= 60:
    a = a+((b+c)//60)
    b = (b+c)-(60*((b+c)//60))
if a >= 24:
    a = a - 24
print(a, b)

