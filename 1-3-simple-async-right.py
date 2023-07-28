# Task A: Computing 0+1
# Time: 0.00
# Task B: Computing 0+1
# Time: 0.00
# Task A: Computing 1+2
# Time: 1.01
# Task B: Computing 1+2
# Time: 1.01
# Task A: Sum = 3

# Task B: Computing 3+2
# Time: 2.02
# Task B: Sum = 5

# Time:3.04 sec

import asyncio
import time
async def sleep():
    #ฟังก์ชั่น sleep() ให้รอ 1 วินาที 
    print(f'Time: {time.time() - start:.2f}')
    await asyncio.sleep(1)

async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        #คำนวณผลรวมตัวเลข
        total += number
    print(f'Task {name}: Sum = {total}\n')

start = time.time()
#กำหนดค่าsum
loop = asyncio.get_event_loop()
tasks = [loop.create_task(sum("A", [1, 2])),
        loop.create_task(sum("B", [1, 2, 2])),
]
#รันloop asyncio.wait
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()
print(f'Time:{end-start:.2f} sec')