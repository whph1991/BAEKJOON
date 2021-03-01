#2839
inp = int(input())
box = 0
while True:
    if(inp % 5) == 0:
        box += (inp//5)
        print(box)
        break
    inp -= 3
    box += 1
    if inp < 0:
        print(-1)
        break