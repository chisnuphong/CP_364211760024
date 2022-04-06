# Lab 8  Exercise

"""
จงกำหนดฟังก์ชัน ชื่อ "getNumber()" เพื่อรับข้อมูลจำนวนเต็มจากผู้ใช้
5 จำนวน และแสดงผลทางจอภาพ จากนั้นให้กำหนดฟังก์ชันต่อไปนี้
และ กำหนดฟังก์ชันชื่อ " totalValue()" เพื่อหาผลรวมของตัวเลขทั้งหมด
"""
def getNumber():
    mynumber = []
    for x in range(5):
        mynumber.append(int(input('Enter integer [{x+1}]: ')))
    return mynumber

def totalValue():
    total = 0
    for x in var:
        total+=x
        return total

mynum = getNumber()
print(f'The date  from user : {mynum}')
print(f'The summation of'
      'thoese integer')


