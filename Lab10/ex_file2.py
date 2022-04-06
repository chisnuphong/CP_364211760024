# File - create and write

"""
mode
x - create
a - create and write from and of file
w - create and overwrite
"""

# create  file write mode 'x'
try:
    f = open("demo5.txt",'x')
    print(f.read())
except Exception as e:
    print(e)
    print("This file name is already exist.")
else:
    print("create file successfull.")

# create  file write mode 'a'
try:
    f = open("demo6.txt", 'a')
    f.write("writing contents with mode 'a' ...MIT211\n")
except Exception as e:
    print(e)
else:
    print('writing contents already.')
finally:
    f.close()
# create  file write mode 'w'
try:
    f = open("demo7.txt", 'w')
    f.write("delete and writing new contents with mode 'w' ")
except Exception as e:
    print(e)
else:
    print('writing contents already.')
finally:
    f.close()
