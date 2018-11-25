a={1:'Sunil',2:'Aunil',3:'Santosh'}
print(a)

del a[3]
print(a)


print(len(a))

b=a.get(1)
print(b)
c=a
print(str(c))
d=a.values()
print(str(d))

ff=5 in a
print(ff)

del a, b

a=[11,21,31,41]
b=['hary','tom','sangappa']
print(a,b)

ab=zip(a,b)
print(ab)
g=dict(ab)
print(g)
l={41:'some'}
g.update(l)
g.update({51:'thing'})

print(g[51])