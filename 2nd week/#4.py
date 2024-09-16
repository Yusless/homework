#4
d=0
w=0
a=list(map(int, input().split()))
for i in range (len(a)):
    s=0
    for k in range(len(a)):
        if a[i] == a[k]:
            s+=1
    if w<s:
        w=s
        d=a[i]
print(d)