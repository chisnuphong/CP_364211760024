# Dictionary key : value

# example
car = {'brand':'Toyota','modle':'vios','year':2021}

# access to data in Dictionary
print('data in Dictionary: ',car)
print('type of variable: ',type(car))
print('Number of data in dictionary:',len(car))

# key
print(car['brand'],type(car['brand']))
print(car['modle'],type(car['modle']))
print(car['year'],type(car['year']))

# get
print(car.get('brand'))
print(car.get('modle'))
print(car.get('year'))

# access to keys  in Dictionary
x = car.keys()
print(x)
print(type(x))

# access to values in dict
x = car.values()
print(x)
print(type(x))

# items
x = car.items()
print(x)
print(type(x))

# loop
for x in car:
    print(x)
for x in  car:
    print(car[x])

# ues keys() with loop
for x in car.keys():
    print(x)

# ues values() with loop
for x in car.values():
    print(x)

# ues items() with loop
for x,y in car.items():
    print(x,y)

# in keyword
if 'coler' in car:
    print('coler is a key in dict.')
else:
    print('There has no coler key in dict')

# change data in dict
print(car)
car['modle'] = 'Altis'
print(car)

# update
car.update({'year':2022})
print(car)

# add data to dict
print(car)

# add coler = 'rad' to dict
car['coler'] = 'rad'
print(car)

# update
car.update({'price':'900k'})
print(car)

# remove data in dict
# pop
if 'price' in car:
    car.pop('price')
else:
    print('Dict has no key -->"price".')
print(car)

# popitem
car.popitem()
print(car)

# del keyword
del car['year']
print(car)

# clear
car.clear()
print(car)



