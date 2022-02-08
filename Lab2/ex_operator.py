# Operator

x = 10
y = 20

# math operator
print('x + y = ', x+y)
print(f'x + y ={x+y}')

print(f'{x}+{y}={x+y}')
print(x,'+',y,'=',x+y)

print(f'{x}-{y}={x-y}')
print(f'{x}*{y}={x*y}')
print(f'{x}/{y}={x/y}')
print(f'{x}**{y}={x**y}')
print(f'{x}%{y}={x%y}')
print(f'{x}//{y}={x//y}')

# comparasion  operators
print(f'{x}=={y} = {x==y}')
print(f'{x}!={y} = {x!=y}')
print(f'{x}>{y} = {x>y}')
print(f'{x}<{y} = {x<y}')
print(f'{x}>={y} = {x>=y}')
print(f'{x}<={y} = {x<=y}')

# logical operators
# and , or , not
print(f'x>20 and x<10 = {x>20 and x<10}')
print(f'x>20 aor x<10 = {x>20 or x<10}')
print(f'not(x>20 or x<10) = {not(x>20 or x<10)}')

# identity operators
# is , is not
x = 100
y = 100
print(f'x is y = {x is y}')
y = 200
print(f'x is y = {x is y}')
print(f'x is not y = {x is not y}')

list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]
print(f'list1 is list2 = {list is list2}')
newlist = list1
print(f'newlist1 is list1 = {newlist is list1}')

# bitwise operators
x = 100
y = 200
print(x & y)
print(f'x & y = {x & y}')
print(f'{x} & {y} = {x & y}')

