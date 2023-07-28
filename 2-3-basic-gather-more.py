# Wed Jul 26 15:08:19 2023hello0started
# Wed Jul 26 15:08:19 2023hello1started
# Wed Jul 26 15:08:19 2023hello2started
# Wed Jul 26 15:08:19 2023hello3started
# Wed Jul 26 15:08:19 2023hello4started
# Wed Jul 26 15:08:19 2023hello5started
# Wed Jul 26 15:08:19 2023hello6started
# Wed Jul 26 15:08:19 2023hello7started
# Wed Jul 26 15:08:19 2023hello8started
# Wed Jul 26 15:08:19 2023hello9started
# Wed Jul 26 15:08:23 2023hello0done
# Wed Jul 26 15:08:23 2023hello2done
# Wed Jul 26 15:08:23 2023hello6done
# Wed Jul 26 15:08:23 2023hello9done
# Wed Jul 26 15:08:23 2023hello8done
# Wed Jul 26 15:08:23 2023hello5done
# Wed Jul 26 15:08:23 2023hello7done
# Wed Jul 26 15:08:23 2023hello4done
# Wed Jul 26 15:08:23 2023hello1done
# Wed Jul 26 15:08:23 2023hello3done
# Time:4.03sec

import asyncio
import time

async def hello(i):
    print(f"{time.ctime()}hello{i}started")
    await asyncio.sleep(4)
    print(f"{time.ctime()}hello{i}done")

async def main():
    coros = [hello(i)for i in range(10)] # สร้างรายการของ coroutines จาก hello(0) ถึง hello(9)
    await asyncio.gather(*coros) # รวม coroutines และรอให้ทุก coroutine เสร็จสิ้น

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())# รัน main() coroutine ด้วย asyncio.run   
    end = time.time()
    print(f'Time:{end-start:.2f}sec') 