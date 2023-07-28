# 1-1-simple-sync.py
# Task A: Computing 0+1
# Time: 0.00
# Task A: Computing 1+2
# Time: 0.00
# Task A: Sum = 3      

# Task B: Computing 0+1
# Time: 0.00
# Task B: Computing 1+2
# Time: 0.00
# Task B: Computing 3+3
# Time: 0.00
# Task B: Sum = 6      

# Time: 0.00 sec

import time

def sleep():
    print(f'Time: {time.time() - start:.2f}')


def sum(name, numbers):
    total = 0
    for number in numbers:
         # แสดงข้อความการคำนวณและตัวเลขที่ใช้ในการคำนวณ
        print(f'Task {name}: Computing {total}+{number}')
        sleep()
        total += number
  # แสดงข้อความการคำนวณและตัวเลขที่ใช้ในการคำนวณ
    print(f'Task {name}: Sum = {total}\n')
# บันทึกเวลาที่เริ่มต้นการทำงานของโปรแกรม
start = time.time()
#เรียกใช้งานฟังก์ชั่น sum() สองครั้งพร้อมกัน
task = [
    sum("A", [1, 2]),
    sum("B", [1, 2, 3],)
]
# บันทึกเวลาที่โปรแกรมทำงานเสร็จสิ้น
end = time.time()
print(f'Time: {end-start:.2f} sec')