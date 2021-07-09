#43
'''
n=int(input('n='))
a=[]
for i in range(n):
    a.append(int(input()))
print(a) 
#1-usul
sanoq=0
for i in range(n-1):
    if a[i]==a[i+1]:
        sanoq+=1
print(n-sanoq)
#2-usul
b=set(a)
print(b)
print(len(b))
'''
#44
'''
#n=int(input('n='))
a=[9, 5, 7, 3, 4, 6, 4, 1]
n=len(a)
for i in range(n):
    a.append(int(input()))
print(a) 
b=[]
sanoq=0
# 
i=0
while i<n-1:
    j=i+1
    while (j<n-1) and (a[i]!=a[j]):
        j+=1
    if a[i]==a[j]:
        print(i,j)
    i+=1
'''
#45
'''
#n=int(input('n='))
a=[9, 5, 7, 3, 4, 6, 4, 1]
n=len(a)
for i in range(n):
    a.append(int(input()))
print(a) 
b=[]
sanoq=0
# 
for i in range(n-1):
    b.append(abs(a[i+1]-a[i]))
    # ayirmalar modulidan hosil bo'lgan ro'yxat
print(a[b.index(min(b))] , a[b.index(min(b))+1])
'''
