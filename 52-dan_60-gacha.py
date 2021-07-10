#52
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
for i in range(n):
    if a[i]<5:
        b.append(2*a[i])
    else:
        b.append(a[i]/2)
print(b)
'''      
#53
'''
import random
n=int(input('n='))
a=[]
b=[]
for i in range(n):
    a.append(random.randrange(1,50))
    b.append(random.randrange(1,50))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 
print(b)
c=[]
for i in range(n):
    c.append(max(a[i],b[i]))
print("Natija")
print(c)
'''
#54
'''
import random
n=int(input('n='))
a=[]
b=[]
for i in range(n):
    a.append(random.randrange(1,50))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 

for i in range(n):
    if a[i] % 2 == 0:
        b.append(a[i])
print('Elementlar soni: ', len(b))        
print(b) #Yangi ro'yxatni chiqarish
'''
#55
'''
# =============================================================================
# import random
# n=int(input('n='))
# a=[]
# b=[]
# for i in range(n):
#     a.append(random.randrange(1,50))
#     #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
# print(a) 
# =============================================================================
a=[9,5,2,5,4,5,6,1]
n=len(a)
b=[]
for i in range(1, n, 2):
    b.append(a[i])

print('Elementlar soni: ', len(b))        
print(b) #Yangi ro'yxatni chiqarish    
'''
#56
'''
import random
n=int(input('n='))
if n<=15:
    a=[]
    c=[]
    b=[]
    for i in range(n):
        a.append(random.randrange(1,50))
        #a.append(int(input()))
        #1-usul
        if (i % 3 == 0)and(i>1):
            c.append(a[i])
    #2-usul            
    for i in range(3,n,3):
        b.append(a[i])   
    print(a)        
    print(c)
    print(b)
    print('Elementlar soni',len(b))
else:
    print('Masala shartiga mos son kiriting!')    
'''
#57
'''
import random
n=int(input('n='))
a=[]
b=[]
for i in range(n):
    a.append(random.randrange(1,50))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 

for i in range(0,n,2):
    b.append(a[i])
    #juft indeksli elementlarni yig'ish
for i in range(1,n,2):
    b.append(a[i])
    #toq indeksli elementlarni yig'ish
print('Elementlar soni: ', len(b))
print(b)
'''
#58
'''
import random
n=int(input('n='))
a=[]
for i in range(n):
    a.append(random.randrange(1,50))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 
s=0
b=[]
#1-usul
for i in range(n):
    s+=a[i]
    b.append(s)
print(b)

#2-usul
c=[a[0]]
for i in range(1,n):
    c.append(c[i-1]+a[i])
print(c)
'''
#59
'''
import random
n=int(input('n='))
a=[]
for i in range(n):
    a.append(random.randrange(1,10))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 
b=[]
s=0
for i in range(n):
    s+=a[i]
    b.append(s/(i+1))
print(b)
'''
#60
'''
import random
n=int(input('n='))
a=[]
for i in range(n):
    a.append(random.randrange(1,10))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a) 
#1-usul
b=[]
s=0
for i in range(n):    
    b.append(sum(a)-s)
    s+=a[i]
print(b)
#2-usul
s=0
c=[]
for i in range(n):
    for j in range(i,n):
        s+=a[j]
    c.append(s)
    s=0
print(c)
'''
