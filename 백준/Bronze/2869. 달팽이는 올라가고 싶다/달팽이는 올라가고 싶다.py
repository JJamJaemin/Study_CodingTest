#A 올라가는것 B 내려가는 것 V 높이
A,B,V = map(int,input().split())

V = V - A
day = V/(A-B)+1
if day % int(day) != 0:
    day = int(day) + 1
print(int(day))