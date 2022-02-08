# raise

def myfunc():
    x = input('Enter an integer:')
    if not type(x) is int:
        raise TypeError('Invalid input:', x)
    else:
        return x*2

try:
    myfunc()
except Exception as e:
    print(e)
    print('Somthing went wrong.')