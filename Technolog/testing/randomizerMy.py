from ast import And
import random 

# print((random.randint(0,460)-230)*0.01)


# print(300 +(random.randint(0,40)-20))
res = 0
mass = [0,0,0,0,0]
mass2 = [0,0,0,0,0]
# print(res<1.734 and res>1.73)
# while not(res<(-0.78) and res>(-0.785)):
for i, val in enumerate(mass):
    mass[i] = 300 +(random.randint(0,40)-20)
    mass2[i] = 300 +(random.randint(0,40)-20)
    # print(val)
s1,s2 = 0, 0
for i, val in enumerate(mass):
    s1+=val
    s2+=mass2[i]
res=100-((s1*100)/s2)
print(res)
print('first:')
for i in mass:
    print(i)
print('second:')
for i in mass2:
    print(i)


print('res = '+ str(res))