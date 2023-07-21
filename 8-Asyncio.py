#example fo runnig a bolcking io-bound task in asynico
import asyncio
import time

#a block io-bound task
def blocking_task():
    #repot  a message
    print(f'{time.ctime()} Task starting')
    #bolck for a while
    time.sleep(2)
    #report a message 
    print(f'{time.ctime()} Task done')

#main coroutine
async def main():
    #report a message 
    print(f'{time.ctime()} Main running the blocking task')
    #create a corotine for the blocking task
    coro = asyncio.to_thread(blocking_task)
    #schedule the task
    task = asyncio.create_task(coro)
    #report a message 
    print(f'{time.ctime()} Main doing ohter things')
    #allow the scheduled task to staet
    await asyncio.sleep(0)
    #await the task
    await task
#run the asyncio program
asyncio.run(main())

# Wed Jul 19 14:52:36 2023 Main running the blocking task
# Wed Jul 19 14:52:36 2023 Main doing ohter things
# Wed Jul 19 14:52:36 2023 Task starting
# Wed Jul 19 14:52:38 2023 Task done