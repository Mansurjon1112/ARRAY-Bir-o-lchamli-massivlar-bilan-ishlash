
#1
"""
n=int(input('n=')) # elementlar soni
l=[] # bo'sh ro'yyxat 
for i in range(1,2*n,2):  
    l.append(i) #elementlarni qo'shish uchun
print(l)    
"""  
#2
"""
n=int(input('n=')) # elementlar soni
l=[] # bo'sh ro'yyxat 
for i in range(n): 
    l.append(2**i) #elementlarni qo'shish uchun
print(l)    
"""
#3
'''
n=int(input('n=')) # elementlar soni
a=int(input('A=')) #Arif prog.ning dastlabki hadi
d=int(input('D=')) #Arif prog.ning ayirmasi
l=[] # bo'sh ro'yyxat
for i in range(n): 
    l.append(a) #elementlarni qo'shish uchun
    a+=d # Arif prog.ning keyingi hadini hosil qilish 
print(l)    
'''
#4
'''
n=int(input('n=')) # elementlar soni
a=int(input('A=')) #Geo prog.ning dastlabki hadi
d=int(input('D=')) #Geo prog.ning maxraji
l=[] # bo'sh ro'yyxat
for i in range(n): 
    l.append(a) #elementlarni qo'shish uchun
    a*=d # Geo prog.ning keyingi hadini hosil qilish 
print(l)  
'''
#5
'''
n=int(input('n=')) # elementlar soni
l=[1,1] # dastlabki 2 elementi bor ro'yxat
for i in range(2,n): 
    l.append(l[i-1]+l[i-2])
    
    #l.insert(i, l[i-1]+l[i-2])
print(l)  
'''
#6
"""
#1-usul
n=int(input('n=')) # elementlar soni
a=int(input('A=')) 
b=int(input('B='))
l=[a,b,a+b] # 
for i in range(2,n-1): 
    l.append(l[i]*2)
print(l)  

#2-usul
n=int(input('n=')) # elementlar soni
a=int(input('A=')) 
b=int(input('B='))
l=[a,b]
for i in range(2,n): 
    s=0
    for j in l:
        s += j
    l.append(s)
print(l)  
"""
#7
'''
n=int(input('n='))
a=[]
print('Massiv elementlarini kiriting: ')
for i in range(n):
    a.append( int(input()) )
print(a)

#teskari chiqarish  1-usul
a.reverse()
print(a)

# 2-usul
print(a[::-1])
'''
#8
'''
n=int(input('n='))
a=[]
b=[]
print('Massiv elementlarini kiriting: ')
for i in range(n):
    a.append( int(input()) )
for i in a:
    if i % 2 == 1:
        b.append(i)
print(b,'Toqlar soni=',len(b) )        
'''
#9
'''
n=int(input('n='))
a=[]
b=[]
print('Massiv elementlarini kiriting: ')
for i in range(n):
    a.append( int(input()) )
for i in a:
    if i % 2 == 0:
        b.append(i)
print(b[::-1],'Juftlar soni=',len(b) )  
'''

#10
'''
n=int(input('n='))
a=[]
b=[]
c=[]
print('Massiv elementlarini kiriting: ')
for i in range(n):
    a.append( int(input()) )
for i in a:
    if i % 2 == 0:
        b.append(i) #Juftlarini aniqlash
    else:
        c.append(i) #Toqlarini aniqlash
b.extend(c[::-1]) #Ro'yxatlarni birlashtirish
print(b)
'''
#11
'''
import random
n=int(input('n='))
a=[]
#print('Massiv elementlarini kiriting: ')
for i in range(n):
    a.append(random.randrange(1,60))
    #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
print(a)

k=int(input('K='))
print(a[k::k])
for i in range(k,n,k):
    print(a[i])
'''
#12
import random
n=int(input('n='))
if n%2==0:
    a=[]
    #print('Massiv elementlarini kiriting: ')
    for i in range(n):
        a.append(random.randrange(1,60))
        #Ro'yxat elementlarini ixtiyoriy to'ldirib olish
    print(a)
    
    k=int(input('K='))
    print(a[0::2])
    for i in range(0,n,2):
        print(a[i])
else:    
    print('Juft son kiritishingiz shart edi!!!')
