a=int(input())
b=int(input())
if b==0:
    exit()
x=abs(a)
y=abs(b)
q=0
while x>=y:
    x-=y
    q+=1
r=x
if (a>0)!=(b>0):
    if r!=0:
        q=-q-1
        r=y-r
    else:
        q=-q
if b<0:
    r=-r
print(q, r)