#3
d=[]
a=list(map(int, input().split()))
for i in range (len(a)):
    s=a.count(a[i])
    if s==1:
        print(a[i])