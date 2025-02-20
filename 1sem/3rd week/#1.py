#
a=int(input('Число:'))
b=2
c=[]
while a!=1:
    if a%b==0:
        a=a//b
        c.append(b)
        b=2
    else:
        b+=1
print(c)