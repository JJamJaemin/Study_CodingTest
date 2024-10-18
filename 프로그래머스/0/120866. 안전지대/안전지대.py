def solution(board):
    answer = 0
    dx = [0,1,0,-1,1,1,-1,-1]
    dy = [1,0,-1,0,1,-1,1,-1]
    boom = []
    
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                boom.append((i,j))
    
    for x, y in boom:
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny <n :
                board[nx][ny] = 1
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                answer += 1
    return answer