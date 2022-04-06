# Function

print('Start')

# define
def functionA():
    print('Hallo from function A.')

def functionB(var):
    print('Hello from function B.', var)

def functionC(var1,var2):
    print('Hello from function C.', var1,var2)

def functionD(*var):
    print('Hello from function D.')
    # for x in var

    #   print(x)
    print(var)

def functionE(var1,var2,var3):
    print('Hello from function E.', var1,var2,var3)

def functionF(**var):
    print('Hello from function F.')
    print(var)


# calling
functionA()
functionB('Saiyai')
functionC('Saiyai','Campus')
functionD(10,'Hello',20.22,True)
# calling Function with
functionE(var3=100,var2=200,var1=300)
functionF(fname='chisnuphong',lname='channual',major='MIT')

print('End')