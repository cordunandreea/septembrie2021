with open('Lista1.txt','r') as f:
    x=list(eval(f.read()))
with open('Lista2.txt','r') as f:
    y=list(eval(f.read()))
c=x[0]+x[1]+x[2]
print(c)
print(sum(x))
v=1
for i in range(len(x)):
    a=x[i]
    v=v*a
print(p)
z=abs(y[3])
print(z)