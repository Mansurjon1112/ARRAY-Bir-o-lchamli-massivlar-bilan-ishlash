#61
'''
import random
n=int(input('n='))
a=[]
for i in range(n):
    a.append(random.randrange(1,5))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 
s=0
sanoq=0
c=[]
for i in range(n):
    for j in range(i,n):
        s+=a[j]
        sanoq+=1
    c.append(s/sanoq)
    s=0
print(c)
'''
#62
'''
import random
n=int(input('n='))
a=[]
for i in range(n):
    a.append(random.randrange(1,5))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 
b=[]
c=[]
for i in range(n):
    if a[i]>0 :
        b.append(a[i])
        #musbat elementlarni yig'ish
    else:
        c.append(a[i])
        #manfiy elementlarni yig'ish
print(b)        
print('Elementlar soni',len(b))
print(c)        
print('Elementlar soni',len(c))
'''
#63
'''
import random
n=5
a=[]
b=[]
for i in range(n):
    a.append(random.randrange(1,5))
    b.append(random.randrange(1,5))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 
print(b)
c=[]
c.extend(a)
c.extend(b)
c.sort()
print(c)
# =============================================================================
# for i in range(n):
#     a.append(b[i])
# a.sort()    
# print(a)
# =============================================================================
'''
#64
# =============================================================================
# 63-misolning 3 taligi 
# d.extend(a)
# d.extend(b)
# d.extend(c)
# =============================================================================

#65
'''
import random
n=int(input('n='))
k=int(input('k='))
a=[]
if 1<=k<=n:
    for i in range(n):
        a.append(random.randrange(1,10))
    print(a)
    m=a[k]
    for i in range(n):
        a[i]+=m
    print(a)        
else:
    print('1<=k<=n shart asosida k ni kiriting!')    
'''
#66
'''
import random
n=int(input('n='))
a=[]
for i in range(n):
    a.append(random.randrange(1,10))
print(a)
m=0
#1-uchragan juft sonni aniqlash (1-usul)
for i in range(n):
    if a[i] % 2 == 0:
        m=a[i]
        break
#1-uchragan juft sonni aniqlash (2-usul)
i=0
while (a[i]%2!=0) and (i!=n-1):
    i+=1
if a[i]%2==0:
    m=a[i]

for i in range(n):
    if a[i]%2==0:
        a[i]+=m
print(a) 
''' 
#67
'''
import random
n=int(input('n='))
a=[]
for i in range(n):
    a.append(random.randrange(1,10))
print(a)
for i in range(n-1,-1,-1):
    if a[i] % 2 == 1:
        m=a[i]
        break
for i in range(n):
    if a[i]%2==1:
        a[i]+=m
print(a) 
'''
#68
'''
import random
n=int(input('n='))
a=[]
for i in range(n):
    a.append(random.randrange(1,10))
print(a)
k=a.index(max(a))
m=a.index(min(a))
a[k],a[m] = a[m],a[k]
print(a)
'''
#69
'''
import random
n=int(input('n='))
if n%2==0:
    a=[]
    for i in range(n):
        a.append(random.randrange(1,10))
    print(a)
    for i in range(0,n,2):
        a[i],a[i+1]=a[i+1],a[i]
    print(a)        
else:
    print('n ga juft son kiriting!')    
'''
#70
'''
import random
n=int(input('n='))
if n%2==0:
    a=[]
    for i in range(n):
        a.append(random.randrange(1,10))
    print(a)
    #1-usul
    for i in range(n//2):
        a[i],a[n//2+i]=a[n//2+i],a[i]
    print(a)        
    #2-usul 
    a[0:n//2],a[n//2:] = a[n//2:], a[0:n//2]
    print(a)   
else:
    print('n ga juft son kiriting!') 
'''
#71
'''
import random
n=int(input('n='))
a=[]
for i in range(n):
    a.append(random.randrange(1,10))
print(a)
a.reverse()
print(a)
'''
#72
!!!

#73
!!!

#74
'''
import random
n=int(input('n='))
a=[]
for i in range(n):
    a.append(random.randrange(1,10))
print(a)
k=a.index(max(a))
m=a.index(min(a))
if m<k:
    k,m=m,k
for i in range(k+1,m):
    a[i]=0       
print(a)
'''
#75
'''
import random
n=int(input('n='))
a=[]
for i in range(n):
    a.append(random.randrange(1,10))
print(a)
k=a.index(max(a))
m=a.index(min(a))
if m<k:
    k,m=m,k
b=a[k:m+1]
b.reverse()        
a[k:m+1]=b
print(a)
'''

