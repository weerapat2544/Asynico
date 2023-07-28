# Task A: Computer 0+1
# Time: 0.00
# Task B: Computer 0+1
# Time: 0.00
# Task A: Computer 1+2
# Task B: Computer 1+2
# Time: 1.01
# Time: 1.01
# Task B: Computer 3+3
# Task A:Sum = 3

# Time: 2.01
# Task B:Sum = 6

# Time: 3.01 sec
import asyncio
import time 
from concurrent.futures.thread import ThreadPoolExecutor
#ฟังก์ชั่น sleep() ให้รอ 1 วินาที
def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)
  # ใช้ ThreadPoolExecutor ด้วยจำนวนเธรดสูงสุดที่ 2 เธรด
async def sum(name, numbers):
    _executor = ThreadPoolExecutor(2)
    total = 0 
    for number in numbers:
        print(f'Task {name}: Computer {total}+{number}')
        await loop.run_in_executor(_executor, sleep)
        total += number
    print(f'Task {name}:Sum = {total}\n')

start =time.time()
#กำหนดค่าsum
loop = asyncio.get_event_loop()
task = [
        loop.create_task(sum("A", [1,2])),
        loop.create_task(sum("B", [1,2,3])),
]
loop.run_until_complete(asyncio.wait(task))
loop.close

end= time.time()
print(f'Time: {end-start:.2f} sec')