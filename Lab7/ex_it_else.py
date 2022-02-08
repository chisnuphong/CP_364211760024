# Login

# username = 'admin'
# password = '1234'

# u = input('Enter username: ')
# p = input('Enter password: ')

# if u == username and p == password:
#    print(f'Welcome {u}')
# else:
#    print('your username or password is not correct. ')

#if u == username:
#    if p == password:
#        print(f'Welcome {u}')
#    else:
#        print(f'your  password is not correct.')
# else:
#    print(f' username is not correct.')

u = input('Enter username: ')
if u ==  username:
    p = input('Enter password: ')
    if p == password:
        print(f'Welcome {u}')
    else:
        print(f'your  password is not correct.')
else:
    print(f' username is not correct.')
