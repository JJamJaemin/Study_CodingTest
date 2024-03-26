def solution(sides):
    max = sides[0]
    side1 = sides[0]
    side2 = sides[0]
    i = 0
    for i in range(3):
        if sides[i] > max:
            max = sides[i]
        elif side1<sides[i]<max:
            side1 = sides[i]
        else:
            side2 = sides[i]
            
    if max<side1+side2:
        answer =1 
    else:
        answer =2

    return answer