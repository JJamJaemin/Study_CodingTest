from itertools import permutations
from collections import deque
A, B, C = map(int, input().split())

#물을 옮길 수 있는 경우 a -> b , a -> c, b -> a, b -> c, c -> a, c -> b
def bfs(A, B, C):
  visited = []
  answer = []
  q = deque()
  q.append((0, 0, C))

  while q:
    a, b, c = q.popleft()

    if [a, b, c] in visited:
      continue
    visited.append([a, b, c])

    if a == 0:
      answer.append(c)

    # A -> B
    if a + b > B:
      q.append((a - (B - b), B, c))
    else:
      q.append((0, a + b, c))

    # A -> C
    if a + c > C:
      q.append((a - (C - c), b, C))
    else:
      q.append((0, b, a + c))

    # B -> A
    if b + a > A:
      q.append((A, b - (A - a), c))
    else:
      q.append((b + a, 0, c))

    # B -> C
    if b + c > C:
      q.append((a, b - (C - c), C))
    else:
      q.append((a, 0, b + c))

    # C -> A
    if c + a > A:
      q.append((A, b, c - (A - a)))
    else:
      q.append((c + a, b, 0))

    # C -> B
    if c + b > B:
      q.append((a, B, c - (B - b)))
    else:
      q.append((a, c + b, 0))

  return sorted(answer)

answer = bfs(A,B,C)
for i in answer:
  print(i, end=" ")
