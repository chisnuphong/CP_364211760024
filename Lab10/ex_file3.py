# File - I-O
# delete file
import os.path

try:
    f = open("")
    print(f.read())
except Exception as e:
    print(e)
finally:
    f.close()

# delete file

if os.path.exists()