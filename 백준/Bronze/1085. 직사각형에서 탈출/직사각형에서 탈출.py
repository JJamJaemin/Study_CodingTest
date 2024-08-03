x,y,w,h = map(int,input().split())

tmp_w = w - x
tmp_h = h - y
min_x = 0
min_y = 0
if tmp_w >= x:
    min_x = x
else:
    min_x = tmp_w
if tmp_h >= y:
    min_y = y
else:
    min_y = tmp_h

if min_x >= min_y:
    print(min_y)
else:
    print(min_x)