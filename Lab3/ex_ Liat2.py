
mylist = [12,23,27,32,43,56,77,89,98,99]
print(mylist, len(mylist))

# เลือกข้อมูลจาก mylist
# มากกว่าหรือเท่ากับ 50
newlist = [x for x in mylist if x >= 50]
print(newlist)

# เลือกข้อมูลจาก mylist
# มากกว่าหรือเท่ากับ 50 แต่น้อยกว่า 80
newlist = [x for x in mylist if x >=50 and x < 80]
print(newlist)

# จากข้อมูล mylist ให้ทำการเปลี่ยนข้อมูล
# ที่มีค่ามากกว่า 50 เป็น 50 ทั้งหมด
print(mylist)
newlist = [x if x < 50 else 50 for x in mylist]
print(newlist)

mylist.reverse()
print(mylist)

mylist.sort()
print(f'sort Low to High :{mylist}')


