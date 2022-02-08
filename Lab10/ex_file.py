# File - I/O

# read file
# r - read content in a file

f = open("demo.txt")
print(f.read())
f.close()
# read 10
f = open("demo.txt")
print(f.read(10))
f.close()
# read one line
f = open("demo.txt",'r')
print(f.readline())
print(f.readline())
print(f.readlines())
f.close()

# case error
try:
    f = open("demo.txt")
    print(f.read())
except Exception as e:
    print(e)
    print("colud not found a file.")
else:
    print("Opening a file.....")
finally:
    f.close()