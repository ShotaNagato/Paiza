h, w, y, x = map(int, input().split())
s = [list(input()) for _ in range(h)]
s[y][x] = "*"


# 上方向
cy = y - 1
while cy >= 0:
    if s[cy][x] == "*":
        for i in range(cy,y):
            s[i][x] = "*"
        break
    cy -= 1

# 下方向
cy = y + 1
while cy < h:
    if s[cy][x] == "*":
        for i in range(y,cy):
            s[i][x] = "*"
        break
    cy += 1
    
# 右方向
cx = x + 1
while cx < w:
    if s[y][cx] == "*":
        for i in range(x,cx):
            s[y][i] = "*"
        break
    cx += 1

# 左方向
cx = x - 1
while cx >= 0:
    if s[y][cx] == "*":
        for i in range(cx,x):
            s[y][i] = "*"
        break
    cx -= 1
    
    
# 出力処理
for i in range(h):
    for j in range(w):
        print(s[i][j],end="")
    print()
