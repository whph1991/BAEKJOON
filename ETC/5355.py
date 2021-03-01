#5355
T = int(input())
for i in range(0, T):
    a = input().split()
    a[0] = float(a[0])
    
    for j in range(1, len(a)):
        if a[j] == '@':
            a[0] = a[0] * 3
        elif a[j] == '%':
            a[0] = a[0] + 5
        elif a[j] == '#':
            a[0] = a[0] - 7
            
    print('%.02f' % a[0])