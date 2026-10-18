n=int(input())
V=[]
k=0
if 1<=n<=30:
    for i in range(n):
        x=int(input())
        if 1<=x<=300:
            V.append(x)
            if x<=30:
                k+=1
        else:
            print("invalid value for speed")
            exit()
    print(max(V)-min(V))
    print(k)
else:
    print("invalid value for cars")
    exit()