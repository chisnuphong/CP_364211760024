"""
เขียนโปรแกรม Login โดยรับ Input จากผู้ใช้
"""
username = 'admin'
password = '1234'
count = 0
while count < 3:
    u = input('Enter username: ')
    p = input('Enter password: ')
    if u == user and p == password:
        print('Hello, {u}')
        break
    else:
        print(f'your username or password is not correct. {count+1}')
        if count < 2:
            print(f'please , login again.')
        count+=1
else:
    print('your account has been locked,.'
          'please contact admin')



