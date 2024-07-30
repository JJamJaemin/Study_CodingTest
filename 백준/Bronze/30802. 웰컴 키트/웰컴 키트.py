#티셔츠 6가지 묶음으로만 주문 가능 묶음 수는 셋째줄에 제시
#펜은 1종류 P자루씩 묶음 주문 가능 or 한자루씩 주문가능
N = int(input())
size = input().split()
T, P = input().split()
T = int(T)
P = int(P)
T_answer = 0
P_answer = 0
for i in size:
    if int(i) >= T:
        if int(i) % T == 0:
            T_answer += int(i) // T
        else:
            T_answer += int(i) // T + 1
    elif int(i) != 0 and int(i) < T:
        T_answer += 1
print(T_answer) #티셔츠 묶음 수

if N < P:
    print(P_answer, N)
elif N == P:
    P_answer += N // P
    N = N % P
    print(P_answer, N)
elif N > P and N % P == 0:
    P_answer += N // P
    N = N % P
    print(P_answer, N)
else:
    P_answer += N // P
    N = N % P
    print(P_answer, N)



