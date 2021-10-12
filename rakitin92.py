n = int(input())
a = list(map(int, input().split()))
i = 0
while len(a)>0:
    if a[i] == max(a):
        del a[i]
    else:
        i+=1
print(*a)