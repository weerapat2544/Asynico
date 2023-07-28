# Computing factorial(2), currently i=2...
# Computing factorial(3), currently i=2...
# Computing factorial(4), currently i=2...
# Computing factorial(3), currently i=3...
# Computing factorial(4), currently i=3...
# Computing factorial(4), currently i=4...
# [2, 6, 24]
# Time: 3.04 sec

import asyncio
import time

async def factorial(n):#คำนวณค่า factorial ของตัวเลข n แบบ asynchronous หากเรียกใช้งาน factorial(n)
    f = 1
    for i in range(2, n + 1):
        print(f"Computing factorial({n}), currently i={i}...")
        await asyncio.sleep(1)#ทำให้ coroutine หยุดการทำงานและรอเวลา 1 วินาที ก่อนที่จะดำเนินการต่อไปในรอบถัดไป
        f *= i
    return f

async def main():
    L = await asyncio.gather(factorial(2),  factorial(3), factorial(4))# รวม coroutines ทั้งหมดที่ระบุเข้าไปในรูปของ factorial
    print(L)    # [2, 6, 24]

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())# รัน main() coroutine ด้วย asyncio.run 
    end = time.time()#บันทึกเวลาที่หยุดการทำงานของโปรแกรม
    print(f'Time: {end-start:.2f} sec')