# Exception

print('Start')

# x = 100
# print(x)
try:
    x = int(input('Enter an integer:'))
    print(x)
except:
    print('Only integer are allow.')
else:
    print('user input:', x)
finally:
    print('finally,process finished.')

print('End')
