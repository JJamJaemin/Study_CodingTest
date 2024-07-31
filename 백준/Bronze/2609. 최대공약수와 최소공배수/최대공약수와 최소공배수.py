#유클리드 호제법
#GCD 최대공약수 x,y를 받았을때 x(큰수) Y(작은수)
#반복문의 조건 작은 수가 0이 아닐때 까지
#반복할때마다 나머지를 작은수에, 작은 수를 큰수에 집어넣는다
def GCD (x, y):
    if y>x:
        x,y = y,x
    while y != 0:
        x,y = y, x % y
    return x

#LCD 최소공배수 x,y 받았을때 x(큰수), y(작은수)
#최소공배수는 두 수의 곱을 최대공약수(GCD)로 나눈 값이다.
def LCD (x, y):
    return int(x * y / GCD(x,y))
x, y = map(int, input().split())

print(GCD(x, y))
print(LCD(x, y))
