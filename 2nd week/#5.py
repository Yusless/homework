#5
d=''
a,b=int(input()), str(input())
for i in range (0,len(b),a):
    s=b[i:i+a]
    d+=s[::-1]
print(d)