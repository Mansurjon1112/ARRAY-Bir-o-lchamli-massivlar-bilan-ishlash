#46
'''
a=[9, 5, 7, 3, 4, 6, 4, 1]
n=len(a)
r=int(input('R='))
i2=0
j2=1
for i in range(n-1):
    for j in range(i+1, n):
        if abs(a[i]+a[j]-r)<abs(a[i2]+a[j2]-r):
            i2=i
            j2=j    
print(a[i2],a[j2])
'''
#47
'''
a=[7,4,2,3,1,4,5,2,4,7]
#n=[7,4,2,3,1,5]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)
'''
