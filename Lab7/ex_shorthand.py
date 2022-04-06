# Short hand


x = 100

# Short hand it
if x>50: print('x > 50')

# Short hand it else
if x>50:
    print('x > 50')
    print('test')
else:
    print('x < 50')

print('x > 50') if x>50 else print('x < 50')
# Short hand it else it
if x<50:
    print('x < 50')
elif x>50:
    print('x > 50')
else:
    print('x = 50')

print('x < 50') if x<50 else print('x > 50') if x>50 else print('x = 50')
