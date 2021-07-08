#13
'''
import random
n=int(input('n='))
if n%2==1:
    a=[]
    #print('Massiv elementlarini kiriting: ')
    for i in range(n):
        a.append(random.randrange(1,60))
        #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
    print(a)    
    print(a[n-2:0:-2])    
else:    
    print('Toq son kiritishingiz shart edi!!!')    
'''
#14
'''
import random
n=int(input('n='))
a=[]
for i in range(n):
    a.append(random.randrange(1,60))
#Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a)    
b=a[0::2]
b.extend(a[1::2])
print(b)
'''
#15
'''
import random
n=int(input('n='))
a=[]
if n%2==0:
    for i in range(n):
        a.append(random.randrange(1,60))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
    print(a)    
    b=a[1::2] #toq indeksli elementlardan iborat to'plam
    b.extend(a[n-2::-2])
    print(b)
else:
    print('Juft son kiritishingiz shart edi!!!')    
'''
#16
'''
import random
n=int(input('n='))
a=[]
for i in range(n):
    a.append(random.randrange(1,60))
#Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 
b=[]
if n %2 == 0:
    for i in range(n//2):
        b.append(a[i])
        b.append(a[n-i-1])
    print(b)    
else:
    for i in range(n//2+1):
        b.append(a[i])
        b.append(a[n-i-1])
    b.pop()
    print(b) 
    
#2-usul 
import random
n=int(input('n='))
a=[]
for i in range(n):
    a.append(random.randrange(1,60))
#Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 
b=[]
s=0
sanoq=0
for i in range(n):    
    if i % 2 == 0 :        
        b.append(a[s])
        s+=1
    else:
        sanoq+=1
        b.append(a[n-sanoq])        
print(b)    
'''
#17 
'''
import random
n=int(input('n='))
a=[]
for i in range(n):
    a.append(random.randrange(1,60))
#Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 
b=[]
sanoq=0
s=0
for i in range(n):    
    if i // 2  % 2 == 0 :        
        b.append(a[s])
        s+=1
    else:
        sanoq+=1
        b.append(a[n-sanoq])        
print(b)    
'''
#18
'''

import random
n=int(input('n='))
a=[]
for i in range(n):
    a.append(random.randrange(1,60))
#Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 
m = a[-1]
i=0
while (a[i]>=m) and (i!=n-1):
    i+=1
if i==n-1:
    print('0')    
else:
    print(a[i])
'''
#19
'''
import random
n=int(input('n='))
a=[]
for i in range(n):
    a.append(random.randrange(1,60))
#Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 
i = 1
while not(a[0]<a[i]<a[-1]) and (i!=n-1):
    i+=1
if i==n-1:
    print('0')    
else:
    print(a[i])
'''
#20
'''
import random
n=int(input('n='))
k=int(input('k='))
l=int(input('l='))
if 0<=k<=l<n:
    a=[]
    for i in range(n):
        a.append(random.randrange(1,60))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
    print(a) 
    print(sum(a[k:l+1]))
else:
    print('Masala shartiga mos k,l,n kiriting!')
'''
#21
'''
import random
n=int(input('n='))
k=int(input('k='))
l=int(input('l='))
if 0<=k<=l<n:
    a=[]
    for i in range(n):
        a.append(random.randrange(1,60))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
    print(a) 
    print(sum(a[k:l+1])/(l-k+1))
    #(l-k+1) l indeksdan k indeskgacha bo'lgan elementlar soni 
else:
    print('Masala shartiga mos k,l,n kiriting!')
'''
#22
'''
import random
n=int(input('n='))
k=int(input('k='))
l=int(input('l='))
if 0<=k<=l<n:
    a=[]
    for i in range(n):
        a.append(random.randrange(1,60))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
    print(a) 
    print(sum(a)-sum(a[k:l+1]))
else:
    print('Masala shartiga mos k,l,n kiriting!')
'''
#23
'''
import random
n=int(input('n='))
k=int(input('k='))
l=int(input('l='))
if 0<=k<=l<n:
    a=[]
    for i in range(n):
        a.append(random.randrange(1,60))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
    print(a) 
    print((sum(a)-sum(a[k:l+1]))/(n-l+k-1))
    #(l-k+1) l indeksdan k indeskgacha bo'lgan elementlar soni 
    #jami elementlardan ayiramiz. n-(l-k+1)=n-l+k-1    
else:
    print('Masala shartiga mos k,l,n kiriting!')
'''
#24
'''
n=int(input('n='))

a=[]
print(n,'ta element kiriting')
for i in range(n):
    a.append(int(input()))
print(a) 
    
d=a[1]-a[0]
i=2
while (a[i]-a[i-1]==d) and (i!=n-1):
    i+=1
if i==n-1:
    print('Arif prog')    
else:
    print('0')    
'''
#25
'''
n=int(input('n='))

a=[]
print(n,'ta element kiriting')
for i in range(n):
    a.append(int(input()))
print(a) 
#1-usul 
q=a[1]/a[0]
i=2
while (a[i]/a[i-1]==q) and (i!=n-1):
    i+=1
if i==n-1:
    print('Geo prog')    
else:
    print('0')  

#2-usul 
i=1
while a[i]**2==a[i-1]*a[i+1] and i!=n-2:
    i+=1
if i==n-2:
    print('Geo prog')    
else:
    print('0')     
'''    










