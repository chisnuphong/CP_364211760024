# set

myset = {'appie','banana','cherry'}
print(myset)
print(type(myset))
print(len(myset))

# for
for x in myset:
    print(x)

# keyword in
print('appie' in myset)
print('mango' in myset)

# add ()
myset.add('mango')
print(myset)

# update ()
mynum = {10,20,30}
print(mynum)
myset.update(mynum)
print(myset)

# remove
myset.remove('banana')
print(myset)

# discard
myset.discard(20)
print(myset)

# pop
x = myset.pop()
print(x)
print(myset)

# del keword
del mynum
# print(mynum)

# clear
myset.clear()
print(myset)

myset.add(100)
print(myset)