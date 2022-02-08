"""
Name: {นายชิษณุพงศ์  จันทร์นวล}
SID: {364211760024}
Group: {MIT211}
"""

"""
Question 1:
จงเขียนโปรแกรมจากจากคำสั่งต่อไปนี้
(10 คะแนน)
"""

# ประกาศตัวแปร x มีค่าเท่ากับ 100
x = 100
# แสดงผลค่าตัวแปร x
print(x)
# แสดงชนิดข้อมูลของตัวแปร x
print(type(x))

# ประกาศตัวแปร  y มีค่าเท่ากับ 200
y = 200
# แสดงผลค่าตัวแปร y
print(y)
# แสดงชนิดข้อมูลของตัวแปร y
print(type(y))

# แสดงผลค่าตัวแปร x และ y โดยมีข้อความดังนี้  "x is 100 and y is 200" 
print("x is 100 and y is 200",x,y)
# ประกาศตัวแปร z มีค่าเท่ากับ ตัวแปร x ลบด้วยตัวแปร y
z = x-y
# แสดงผลค่าตัวแปร z โดยมีข้อความดังนี้  "z is {z}" โดยการใช้ formatted print  -- > print(f{...})
print(f'z is {z}',x-y)
# หาผลรวมของตัวแปร x, y และ z เก็บไว้ในตัวแปร total
total = x+y+z
print(total)

# แสดงผลค่าตัวแปร total โดยการใช้ formatted print  -- > print(f{...})
print(f'{total}')
# หาผลลบของตัวแปร x, y และ z เก็บไว้ในตัวแปร total
total = {x - y -z }
# แสดงผลค่าตัวแปร total formatted print  -- > print(f{...})
print(f'{total}')
# หาผลคูณของตัวแปร x, y และ z เก็บไว้ในตัวแปร total
print(f'{x}*{y}*{z}={x*y*z}')
# แสดงผลค่าตัวแปร z formatted print  -- > print(f{...})
print(f'z = {x*y*z}')

# หาผลหารของตัวแปร x, y และ z เก็บไว้ในตัวแปร total
print(f'{x}/{y}/{z}={x/y/z}')
# แสดงผลค่าตัวแปร total formatted print  -- > print(f{...})
print(f'total = {x/y/z}')
# หาผลหารแบบจำนวนเต็ม (floor division) ของตัวแปร x, y และ z เก็บไว้ในตัวแปร total
print(f'{x}//{y}//{z}={x//y//z}')
# แสดงผลค่าตัวแปร total formatted print  -- > print(f{...})
print(f'total = {x//y//z}')
