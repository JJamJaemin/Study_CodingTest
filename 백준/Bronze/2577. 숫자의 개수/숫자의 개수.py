A = int(input())
B = int(input())
C = int(input())
answer = A * B * C
list = [0,0,0,0,0,0,0,0,0,0]
for i in str(answer):
    if i == '0':
        list[0] += 1
    elif i == '1':
        list[1] += 1
    elif i == '2':
        list[2] += 1
    elif i == '3':
        list[3] += 1
    elif i == '4':
        list[4] += 1
    elif i == '5':
        list[5] += 1
    elif i == '6':
        list[6] += 1
    elif i == '7':
        list[7] += 1
    elif i == '8':
        list[8] += 1
    elif i == '9':
        list[9] += 1
    
for j in list:
    print(j)
