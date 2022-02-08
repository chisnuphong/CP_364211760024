# Tuple

mytuple = (10,20,30,40,50)
print(mytuple[0])

# tuple - list
mylist = list(mytuple)
print(mylist,type(mylist),len(mylist))

# 0 to 100
mylist[0] = 100
print(mylist)
# 1000
mylist.append(1000)
print(mylist)

# list - tuple
mytuple = tuple(mylist)
print(mytuple,type(mytuple))

# remove
# tuple - list
mylist = list(mytuple)
# remove 50
mylist.remove(50)
print(mylist)
# list - tuple
mytuple = tuple(mylist)
print(mytuple)

#
x = (1,2,3,4,5)
y = ('a','b','c')
print(f'x = {x} y = {y}')

# +
z = x+y
print(f'z = x+y = {z}')

# *
x = x*2
print(x)
y = y*3
print(y)


