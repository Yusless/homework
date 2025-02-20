#4
d=0
m=0
a=list(map(int, input().split()))
for i in range (len(a)):
    s=a.count(a[i])
    if d<s:
        d=s
        m=a[i]
print(m)