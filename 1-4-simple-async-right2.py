# Task A: Computing 0+1
# Time: 0.00
# Task B: Computing 0+1
# Time: 0.00
# Task A: Computing 1+2
# Time: 1.01
# Task B: Computing 1+2
# Time: 1.01
# Task A: Sum = 3

# Task B: Computing 3+3
# Time: 2.03

import asyncio
import time
#ฟังก์ชั่น sleep() ให้รอ 1 วินาที
async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1)

async def sum(name, numbers):
    total = 0
    #เก็บผลรวมตัวเลขในlist
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        #คำนวณผลรวมตัวเลข
        total += number
    print(f'Task {name}: Sum = {total}\n')
#เรียกใช้งานฟังก์ชันที่เป็น Asynchronousและเริ่มทำงาน Task
async def main():
    await asyncio.gather(sum("A", [1, 2]), sum("B", [1, 2, 3]))
#ตรวจสอบและเรียกใช้งาน
if __name__ == '__main__':
    start = time.time()
    asyncio.run(main()) # รัน main() coroutine ด้วย asyncio.run
    end = time.time()
    print(f'Time: {end-start:.2f} sec')