#H:층수 W: 방수 N: 몇번째

N = int(input())
for i in range(N):
    H,W,N = map(int,input().split())
    hotel = [[0 for j in range(W)]for c in range(H)]

    for A in range(H):
        step = 100 * (A + 1) + 1
        for B in range(W):
            hotel[A][B] = step + B
    #층, 호수
    if N <= H:
        print(hotel[N-1][0])
    elif N == H * W:
        print(hotel[-1][-1])
    elif N % H == 0 and N > H:
        print(hotel[-1][N // H -1])
    else:
        stair = N % H # 0
        room = N // H # 9
        print(hotel[stair-1][room])





