# Wed Jul 26 15:07:37 2023 hello 1 started
# Wed Jul 26 15:07:37 2023 hello 2 started
# Wed Jul 26 15:07:41 2023 hello 1 done
# Wed Jul 26 15:07:41 2023 hello 2 done
# Time: 4.01 sec

import asyncio
import time

async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")

async def main():
    task1 = asyncio.create_task(hello(1)) # return immediately, the task is created
    #await asyncio.sleep(3)
    task2 = asyncio.create_task(hello(2))# สร้าง task สำหรับ coroutine hello(2)
    await asyncio.gather(task1, task2)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())# รัน main() coroutine ด้วย asyncio.run
    end = time.time()
    print(f'Time: {end-start:.2f} sec')