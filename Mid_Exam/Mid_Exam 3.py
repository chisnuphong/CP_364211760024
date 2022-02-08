"""
Name: {นายชิษณุพงศ์  จันทร์นวล}
SID: {364211760024}
Group: {MIT211}
"""

"""
Question 3:
จงเขียนโปรแกรมจาก dictionary ที่กำหนดให้
(10 คะแนน)
"""

mydict = {'brand':'toyota','model':'cross','year':'2021'}

# แสดงข้อมูลทั้งหมดใน dicionary mydict
print(mydict)
# แสดงชนิดข้อมูลตัวแปร mydict
print(type(mydict))
# แสดงชนิดข้อมูลค่า value ทุกตัวใน mydict
print(mydict['brand'],type(mydict['brand']))
print(mydict['model'],type(mydict['model']))
print(mydict['year'],type(mydict['year']))
# เพิ่มข้อมูล 'color':['white','black'] ใน mydict
mydict['color']= ['white','black']
print(mydict)
# เพิ่มข้อมูล 'hp': 150 ใน mydict
mydict.update({'hp': 150})
print(mydict)
# แสดงข้อมูลเฉพาะ keys ใน mydict
for x in mydict.keys():
    print(x)
# แสดงข้อมูลเฉพาะ values ใน mydict
for x in mydict.values():
    print(x)
# คัดแยกข้อมูล keys จาก mydict มาเก็บไว้ใรตัวแปรชนิด list ชื่อ mykeys และแสดงข้อมูลทางหน้าจอ
mydict = {}
# คัดแยกข้อมูล values จาก mydict มาเก็บไว้ใรตัวแปรชนิด list ชื่อ myvalues และแสดงข้อมูลทางหน้าจอ
# ลบข้อมูล key: 'hp'

# เปลี่ยนแปลงข้อมูลจากเดิม 'color': ['white','black'] เป็น 'Red'
# แสดงข้อมูล mylist ทางหน้าจอภาพ

