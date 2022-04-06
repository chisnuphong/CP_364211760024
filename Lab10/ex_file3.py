# File - I-O
# delete file
import os.path

try:
    f = open("C:\\Users\ACER\Desktop\demo.desktop.txt")
    print(f.read())
except Exception as e:
    print(e)
finally:
    f.close()

# delete file

if os.path.exists("C:\\Users\ACER\Desktop\demo.desktop.txt"):
    os.remove("C:\\Users\ACER\Desktop\demo.desktop.txt")
else:
    print('Could not find a file.')