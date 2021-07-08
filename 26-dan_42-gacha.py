#26
'''
import random
n=int(input('n='))
a=[]
for i in range(n):
    #a.append(random.randrange(1,60))
    a.append(int(input()))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 
i=0
#1-usul
while (a[i]%2==0) and (a[i+1]%2==1) or (a[i]%2==1) and (a[i+1]%2==0) and (i!=n-1):
    print(a[i],a[i+1])
    i+=1
 
#2-usul
while (a[i]%2!=a[i+1]%2) and (i!=n-1):
    print(a[i],a[i+1])
    i+=1
   

if i==n-1 : 
    print(0)
else:
    print(i)    
'''

#27
'''
#import random
n=int(input('n='))
a=[]
for i in range(n):
    #a.append(random.randrange(1,60))
    a.append(int(input()))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 
i=0

while a[i] * a[i+1] < 0 :
    print(a[i],a[i+1])
    i+=1
    if  i==n-1:
        break

if i==n-1 : 
    print(0)
else:
    print(i)    
'''
#28
'''
import random
n=int(input('n='))
a=[]
for i in range(n):
    a.append(random.randrange(1,60))
    #a.append(int(input()))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 
print(a[::2]) #Juft indeksli elementlar ro'yxati
print(min(a[::2])) #eng kichigi
'''
#29
'''
import random
n=int(input('n='))
a=[]
for i in range(n):
    a.append(random.randrange(1,60))
    #a.append(int(input()))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 
print(a[1::2]) #Juft indeksli elementlar ro'yxati
print(max(a[1::2])) #eng kattasi
'''
#30
'''
import random
n=int(input('n='))
a=[]
for i in range(n):
    a.append(random.randrange(1,60))
    #a.append(int(input()))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 
sanoq=0

for i in range(n-1):
    if a[i]>a[i+1]:
        sanoq+=1
        print(i)
print(sanoq,'ta')        
'''
#31
'''
import random
n=int(input('n='))
a=[]
for i in range(n):
    a.append(random.randrange(1,60))
    #a.append(int(input()))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 
sanoq=0

for i in range(n-1,0,-1):
    if a[i]>a[i-1]:
        sanoq+=1
        print(i)
print(sanoq,'ta')  
'''
#32
'''
import random
n=int(input('n='))
a=[]
for i in range(n):
    a.append(random.randrange(1,60))
    #a.append(int(input()))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 
sanoq=0

for i in range(1,n-1):
    if a[i-1]>a[i]<a[i+1]:
        sanoq+=1
        print(i)
print(sanoq,'ta')  
'''
#33
'''
import random
n=int(input('n='))
a=[]
for i in range(n):
    a.append(random.randrange(1,60))
    #a.append(int(input()))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 
sanoq=0

for i in range(1,n-1):
    if a[i-1]<a[i]>a[i+1]:
        sanoq+=1
        print(i)
print(sanoq,'ta')  
'''
#34
'''
import random
n=int(input('n='))
a=[]
for i in range(n):
    a.append(random.randrange(1,60))
    #a.append(int(input()))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 
sanoq=0
b=[]
for i in range(1,n-1):
    if a[i-1]>a[i]<a[i+1]:
        sanoq+=1
        b.append(a[i])
        #2-usul
        #if sanoq == 1:
        #    m=a[i]
        #elif m < a[i]:
        #    m=a[i]
print(b)        
print(max(b))  
print(m) #2-usulning javobi
'''
#35
'''
import random
n=int(input('n='))
a=[]
for i in range(n):
    a.append(random.randrange(1,60))
    #a.append(int(input()))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 
sanoq=0
b=[]
for i in range(1,n-1):
    if a[i-1]<a[i]>a[i+1]:
        sanoq+=1
        b.append(a[i])
        #2-usul
        #if sanoq == 1:
        #    m=a[i]
        #elif m > a[i]:
        #    m=a[i]
print(b)        
print(min(b))  
print(m) #2-usulning javobi
'''
#36
'''
import random
n=int(input('n='))
a=[]
for i in range(n):
    a.append(random.randrange(1,60))
    #a.append(int(input()))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 
b=[]
for i in range(1,n-1):
    if not((a[i-1]<a[i]>a[i+1])or(a[i-1]>a[i]<a[i+1])):
        b.append(a[i])
print(b)    
if len(b)>0:
    print(max(b))  
else:
    print(0)    
'''
#37
'''
# MONOTON O'SUVCHI ORALIQ HAQIDA 
#import random
n=int(input('n='))
a=[]
sanoq=0
for i in range(n):
    #a.append(random.randrange(1,60))
    a.append(int(input()))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 
b=[]
for i in range(n-1):
    if a[i]>0 and  a[i+1]<0:
        sanoq+=1
print(sanoq)
'''
#40
'''
import random
n=int(input('n='))
r=int(input('R='))
a=[]
for i in range(n):
    a.append(random.randrange(1,60))
    #a.append(int(input()))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 
b=[]
#1-usul 
for i in range(n):
    b.append(abs(a[i]-r))
print(b) #AYirmalar natijasidan hosil bo'lgan ro'yxat 
print( a [b.index(min(b))] )

#2-usul
m=abs(a[0]-r)
natija = a[0]
for i in range(1,n):
    if m>abs(a[i]-r):
        m=abs(a[i]-r)
        natija=a[i]
print(natija)        
'''
#41
'''
import random
n=int(input('n='))
a=[]
for i in range(n):
    a.append(random.randrange(1,60))
    #a.append(int(input()))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 
b=[]
for i in range(n-1):
    b.append(a[i]+a[i+1])    
print(b)
print( a [b.index(max(b))], a[b.index(max(b))+1])
'''
#42
'''
import random
n=int(input('n='))
r=int(input('R='))
a=[]
for i in range(n):
    a.append(random.randrange(1,60))
    #a.append(int(input()))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 
b=[]
#1-usul 
for i in range(n-1):
    b.append(abs(a[i]+a[i+1]-r))
print(b) #AYirmalar natijasidan hosil bo'lgan ro'yxat 
print( a [b.index(min(b))],  a [b.index(min(b))+1] )
'''      
