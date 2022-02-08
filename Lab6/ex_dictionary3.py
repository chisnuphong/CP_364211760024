# Nested Dictionary

car1 = {'brand':'Toyota','modle':'Altis'}
car2 = {'brand':'Honda','modle':'HRV'}
car3 = {'brand':'Mazda','modle':'Mazda 3'}

mycar = {'c1':car1,
         'c2':car2,
         'c3':car3}

print(mycar['c1'])
print(mycar['c2'])
print(mycar['c3'])

print(mycar['c1']['modle'])

car1['coler'] = ['black','rad']

print(mycar['c1'])
print(mycar['c1']['coler'])
print(mycar['c1']['coler'][0])