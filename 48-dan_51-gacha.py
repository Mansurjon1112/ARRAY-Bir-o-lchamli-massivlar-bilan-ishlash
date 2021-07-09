#48
'''
a=[7,4,2,3,1,4,4,4,4,7]
#1-usul
b=[]
for i in a:
    b.append(a.count(i))
print(max(b))    

#2-usul 
m=a.count(0)
for i in a[1:]:
    if m<a.count(i):
        m=a.count(i)
print(m)   
'''
#49
'''
a=[9,3,5,2,4]
n=5
# =============================================================================
# n=int(input('n='))
# a=[]
# for i in range(n):
#     a.append(int(input()))
# print(a) 
# =============================================================================
m=0
for i in range(n):
    if 1<=a[i]<=n and a.count(a[i])==1:
        continue
    else:
        m=1
        break
if m==1 :
    print(i,'indeks')
else:
    print(0)
'''
#50
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
print(sanoq,'ta')        
'''
#51
a=[1,2,5,6,7,9]
b=[4,4,4,4,4,4]
print(a,b)
a,b=b,a
print(a,b)
