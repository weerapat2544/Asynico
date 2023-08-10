"""
การรัน Task หรือ Coroutine พร้อมกันหลายตัว
เราสามารถใช้ method ในการรัน task หรือ coroutine พร้อมกันหลายงานได้ โดยผมจะขอยกตัวอย่างมา 3 ตัว คือ
1. asyncio.gather()
2. asyncio.wait()
3. asyncio.as_completed()


ซึ่งความแตกต่างระหว่าง 2 ตัวนี้ คือ
- asyncio.gather() จะรันเรียงตามลำดับก่อนหลัง ส่วน asyncio.wait() และ asyncio.as_completed() นั้นไม่เรียง
- asyncio.gather() ไม่สามารถกำหนด timeout ได้ แต่ asyncio.wait() กำหนดได้ผ่านพารามิเตอร์ timeout
- asyncio.wait() สามารถกำหนดเงื่อนไขในการรอได้โดยใช้พารามิเตอร์ return_when
- asyncio.gather() ไม่สามารถรับค่าเป็น list ของ coroutine/task ได้โดยตรงแบบ asyncio.wait() ให้ใช้ * หน้า list เพื่อกระจายเป็น argument แทน
- asyncio.as_completed() จะใช้กับ for Loop ซึ่งไม่เหมือนตัวอื่น และเป็น for Loop ที่ทุกรอบเริ่มทำงานพร้อมกัน

จงเปรียบเทียบผลของการสร้าง Task ระหว่าง gather(), wait() และ as_completed()

"""

import asyncio
import time

async def cook(food, t):
    

async def main():
    

if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time() - t1
    print(f'Executed in {t2:0.2f} seconds.')