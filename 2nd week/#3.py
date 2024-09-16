#3
d=[]
a=list(map(int, input().split()))
for i in range (len(a)):
    s=0
    for k in range(len(a)):
        if a[i] == a[k]:
            s+=1
    if s==1:
        d.append(a[i])
print(d)