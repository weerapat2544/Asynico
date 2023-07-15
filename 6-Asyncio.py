#example of waiting for a corouttin  with a timeout
from random import random
import asyncio
import time

#corout to execute in a new task
async def task_coro(arg):
    #generate a randome value between o and 1
    value = 1 + random()
    #report message
    print(f'{time.ctime()} >task got {value}')
    #block for a moment
    await asyncio.sleep(value)
    #repor all tome
    print(f'{time.ctime()} >task done')

#main coroutine
async def main():
    #create a task
    task = task_coro(1)
    #executs and wiat for the task without a timeout
    try:
        await asyncio.wait_for(task, timeout=0.2)
    except asyncio.TimeoutError:
        print(f'{time.ctime()} Gave up waiting, task canceled')
    
#start the asynico program
asyncio.run(main())