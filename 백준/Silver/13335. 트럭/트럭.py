from collections import deque
n,w,l = map(int,input().split()) # n: 자동차 개수 # w : 다리 길이  # l : 최대 하중
car = list(map(int,input().split()))
bridge = [0] * w
car_deque = deque(car)
bridge_deque = deque(bridge)

answer = 0

while car_deque or sum(bridge_deque) != 0:
    #다리 위에 올라 갈 수 있는 경우 (1.차가 추가 2.차가 빠지고)
    if len(car_deque) != 0:
        if sum(bridge_deque) + car_deque[0] <= l:
            bridge_deque.append(car_deque.popleft())
            bridge_deque.popleft()
            answer += 1
        else: #지나갈때 까지 차가 다리에 추가 못하는 경우
            bridge_deque.append(0)
            bridge_deque.popleft()
            answer += 1
            # 차가 빠져나가면서 차가 추가되는 경우
            if sum(bridge_deque) + car_deque[0] <= l and bridge_deque[-1] == 0:
                bridge_deque[-1] = car_deque.popleft()
    else: #추가될 차는 없고 다리에 차가 있을경우
        bridge_deque.append(0)
        bridge_deque.popleft()
        answer += 1
print(answer)


