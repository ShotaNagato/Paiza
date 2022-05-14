# coding: utf-8
h, w, n = map(int, input().split())

s = [list(input()) for _ in range(h)]

def check_row(y,x,s,turn):
    for lr in range(-1,2,2):
        i = 0
        while True:
            i += 1
            if x + i*lr < 0 or x + i*lr >= w or s[y][x+i*lr] == "#":
                break
            if s[y][x+i*lr] == turn:
                for j in range(i):
                    s[y][x+j*lr] = turn
                break
    
def check_column(y,x,s,turn):
    for du in range(-1,2,2):
        i = 0
        while True:
            i += 1
            if y + i*du < 0 or y + i*du >= h or s[y+i*du][x] == "#":
                break
            if s[y+i*du][x] == turn:
                for j in range(i):
                    s[y+j*du][x] = turn
                break

def check_diagonal(y,x,s,turn):
    for du in range(-1,2,2):
        for lr in range(-1,2,2):
            i = 0
            while True:
                i += 1
                if x + i*lr < 0 or x + i*lr >= w or y + i*du < 0 or y + i*du >= h or s[y+i*du][x+i*lr] == "#":
                    break
                if s[y+i*du][x+i*lr] == turn:
                    for j in range(i):
                        s[y+j*du][x+j*lr] = turn
                    break

for i in range(n*2):
    turn = "A"
    if i % 2 != 0:
        turn = "B"
    y, x = map(int, input().split())
    s[y][x] = turn
    
    check_row(y,x,s,turn)
    check_column(y,x,s,turn)
    check_diagonal(y,x,s,turn)
    
for i in range(h):
    for j in range(w):
        print(s[i][j],end="")
    print()
    