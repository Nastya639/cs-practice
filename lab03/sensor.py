limit=float(input())
n=int(input())
ke,kl,mx,avgsum,avgk=0,0,float('-inf'),0,0
for i in range(n):
    x=input()
    if x=='error':
        ke+=1
        continue
    x=float(x)
    if x>limit:
        kl+=1
    if x>=mx:
        mx=x
    avgsum+=x
    avgk+=1
print(n)
print(ke)
print(kl)
print(f'{mx:.1f}')
print(f'{avgsum/avgk:.1f}')
    
