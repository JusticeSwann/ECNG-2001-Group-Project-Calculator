from fourier import *


print("ak values")
for x in range(1,13):
    print(round(ak_1(1,x),2))

print("-----------------------------")
print("bk values")
for x in range(1,13):
    print(round(bk_1(1,x),2))

print("-----------------------------")
print("ck values")
for x in range(1,13):
    print(round(ck_1(1,x),2))


print("-----------------------------")
print("theta_k values")
for x in range(1,13):
    print(round(theta_1(1,x),2))