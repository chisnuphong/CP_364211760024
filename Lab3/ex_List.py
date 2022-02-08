

x = 100
print(x)
x = 200
print(x)

mylist = ['apple','banana','cherry']
print(mylist , type(mylist))
print(f'Length of mylist = {len(mylist)}')

print(mylist[0])
print(mylist[1])
print(mylist[2])

print(mylist[-1])
print(mylist[-2])
print(mylist[-3])

mynum = [10, 20, 30, 40, 50, 60, 70, 'MIT211']
print(mynum)
print(mynum[2:4])
print(mynum[1:6])
print(mynum[:5])
print(mynum[3:])

print(mynum[-5:-1])

for x in mynum:
    print(x,type(x))

for x in range(len(mynum)):
    print(mynum[x])

i = 0
while i <len (mynum):
    print(mynum[i])
    i+=1

mynum[-1] = 80
print(mynum)
mynum[7] = 100
print(mynum)
mynum[0:3] = [100, 200, 300]
print(mynum)
mynum[3:5] = [400, 500, 600]
print(mynum)
mynum[3:6] = [1000]
print(mynum)

mynum.append(10)
print(mynum)

mynum.insert(0,5)
print(mynum)

mynum.remove(10)
print(mynum)
mynum.remove(100)
print(mynum)

mynum.pop(3)
print(mynum)
mynum.insert(0,100)
print(mynum)
mynum.pop(-1)
print(mynum)

del mynum[1]
print(mynum)
# del mynum
# print(mynum)

print(f'all data in mynum = {mynum}')
mynum.clear()
print(mynum)
