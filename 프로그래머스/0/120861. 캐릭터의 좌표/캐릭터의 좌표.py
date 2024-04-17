def solution(keyinput, board):
    answer = []
    tmp = [0,0]
    for i in keyinput:
        if i == 'left' and (tmp[0]-1)*2 >= board[0]*-1:
            tmp[0] -= 1
            print(tmp)
        if i == 'right' and (tmp[0]+1)*2 <= board[0]:
            tmp[0] += 1
            print(tmp)
        if i == 'up' and (tmp[1]+1)*2 <= board[1]:
            tmp[1] += 1
            print(tmp)
        if i == 'down' and (tmp[1]-1)*2 >= board[1]*-1:
            tmp[1] -= 1
            print(tmp)
    answer = tmp
    return answer