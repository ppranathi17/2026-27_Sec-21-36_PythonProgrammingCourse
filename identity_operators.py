a=[1,2,3,4]
b=[1,2,3,4]
c = a is b
print("result of c is:",c)

a = [25,26,27]
b = a
c = a is b
print("result of c is:",c)

# is not
a = [32,34,36]
b = [32,34,36]
c = a is not b
print("result of c is:",c)

x = [100,200,300]
y =x
z= x is not y
print("result of z is:",z)