# set

x = {'a','b','c','d','e'}
y = {10,20,30,40,50}

# join set
# union
z = x.union(y)
print(z,len(z))

# update
x.update(y)
print(x,len(x))

x = {10,20,30,40,50}
y = {40,50,50,70,80}

# intersection
z = x.intersection(y)
print(z)

# intersection_update
x.intersection_update(y)
print(x)

# difference
# symmtric_difference
z = x.symmetric_difference(y)
print(z)

# symmtric_difference_update
x.symmetric_difference_update(y)
print(x)

x = {10,20,30}
y = {20,30,40}
z = x.difference(y)
print(z)

x = {10,20,30,40,50}
y = {30,40,50}
# issubset
y.issubset(x)
print(y.issubset(x))

# issupterset
print(x.issuperset(y))

# isdisjoint
print(x.isdisjoint(y))
print(y.isdisjoint(x))