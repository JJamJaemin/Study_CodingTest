from collections import Counter

# 입력 받기
N = int(input())  # 상근이가 가진 숫자 카드의 개수
sanggeun_cards = list(map(int, input().split()))  # 상근이가 가진 숫자 카드들

M = int(input())  # 몇 개를 가지고 있는지 구해야 할 숫자들의 개수
check_cards = list(map(int, input().split()))  # 확인할 숫자들

# 상근이가 가진 카드의 숫자를 카운팅
card_count = Counter(sanggeun_cards)

# 결과 출력
result = []
for card in check_cards:
    result.append(str(card_count[card]))

print(" ".join(result))
