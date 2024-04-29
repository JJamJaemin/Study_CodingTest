# def solution(n):
#     answer = 0
#     a=[]
#     for i in range(1,100):
#         if str(i).find('3') == -1  and i % 3 !=0:
#             a.append(i)
            
#     answer = a[n-1]
#     return answer

def solution(n):
    answer = 0
    a = list(filter(lambda x:x%3 != 0 and str(x).find('3') == -1,range(1,3*n)))
    answer = a[n-1]
    return answer