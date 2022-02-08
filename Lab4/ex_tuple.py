# Tuple

mytuple = ('apple','banana','cherry')
print(mytuple)
print(type(mytuple))
print(f'Lenght of mytuple is : {len(mytuple)}')

print(mytuple[0])
print(mytuple[1])
print(mytuple[2])

print(mytuple[-1])
print(mytuple[-2])
print(mytuple[-3])

mynum = (10,20,30,40,50)
print(mynum[1:3])
print(mynum[:3])
print(mynum[1:])
print(mynum[-5:-2])

# for
for x in mynum:
    print(x)

# for with
for x in range(len(mynum)):
    print(mynum[x])

# while
i = 0
while i < len(mynum):
    print(mynum[i])
    i +=1
    

