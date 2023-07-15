#example of using asynico shoeld to protect a task from cancellation
import time
import asyncio

#define a simple asynchronous
async def simple_task(number):
    #block for a momber
    await asyncio.sleep(1)
    #return the argument
    return number

#cancel the given  task after a momnet
async def cancel_task(task):
    #block for a moment
    await asyncio.sleep(0.2)
    #cancel the task
    was_canceled = task.cancel()
    print(f'{time.ctime()} canceled: {was_canceled}')

#define a simple corotine
async def main():
    #create the corotine
    coro = simple_task(1)
    #create a task 
    task = asyncio.create_task(coro)
    #create the shielded task
    shielded = asyncio.shield(task)
    #create the task to cancel the previous task
    asyncio.create_task(cancel_task(shielded))
    #handel cancellation
    try:
        #await the shielede task
        result = await shielded
        print(f'{time.ctime()} >got: {result}')
    except asyncio.CancelledError:
        print(f'{time.ctime()} shielded: {shielded}')
        #wait a moment
        await asyncio.sleep(1)
        #report the details of the tasks
        print(f'{time.ctime()} shielded:{shielded}')
        print(f'{time.ctime()} task: {task}')

        #start the loop
        asyncio.run(main())