import numpy as np
import uncertainties as unc
from uncertainties import ufloat

def rel_unc(number):
    return number.s / abs(number.n)


#opgave 1
x=ufloat(95.8,0.1)
y=ufloat(2.3,0.02)
l=x-y 
print('opgave 1a '+str(l))
print('opgave 1b '+str(rel_unc(l)))

#opgave 2
v1=ufloat(14.0,(14*0.01))
v2=ufloat(18.0,(18*0.01))
deltav=v2-v1

v3=ufloat(19,(0.01*19))
v4=ufloat(19.6,(0.01*19.6))
deltav2=v4-v3

print('opgave 2a '+str(rel_unc(deltav)))
print('opgave 2b '+str(rel_unc(deltav2)))
#opgave 3
a=ufloat(5,1)
b=ufloat(18,2)
c=ufloat(12,1)
tee=ufloat(3.0,0.5)
m3=ufloat(18,1)
print('opgave 3a '+str(a+b+c) +' og '+str(rel_unc(a+b+c)))
print('opgave 3b '+str(a+b-c) +' og '+str(rel_unc(a+b-c)))
print('opgave 3c '+str(c*tee) + ' og ' +str(rel_unc(c*tee)))
print('opgave 3d '+str((m3*b)/tee) + ' og ' +str(rel_unc((m3*b)/tee)))


#opgave 4
d=ufloat(5.1,0.01)
t=ufloat(6.02,0.02)
fart4=d/t
print('Opgave 4a '+str(fart4))
m=ufloat(0.711,0.002)
impuls=m*fart4
print('Opgave 4b '+str(impuls))

gem=[9.9,9.6,9.5,9.7,9.8]
print(np.mean(gem))