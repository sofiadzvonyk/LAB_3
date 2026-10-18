n=int(input())
a=1
result=1
for i in range (n-1):
    result=result*(a+1)
    a+=1
print(result)