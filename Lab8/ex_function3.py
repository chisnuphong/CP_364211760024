# Lambda

"""
lambda parameters : expression
"""

x = lambda var : var*2
print(x(5))

x = lambda var1,var2 : var1 * var2
print((x(2,4)))

x = lambda *var:[x for x in var if x%2 ==0]
print(x(10,11,12,13,14,15))

# Lambda in other
def myfunction(var):
    return lambda x : x * var

double = myfunction(2)
print(double(10))

trible = myfunction(3)
print(trible())
