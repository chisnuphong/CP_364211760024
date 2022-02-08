# Tuple

mytuple = ('apple','banana','cherry')
print(mytuple,len(mytuple))

# 1
(x,y,z) = mytuple
print(x,y,z)
print(type(x))

# 2 *
mytuple = ('apple','banana','cherry','orange','mango')
(x,y,*z) = mytuple
print(x)
print(y)
print(z)

# 3
(*x,y,z) = mytuple
print(x)
print(y)
print(z)