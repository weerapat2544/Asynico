# example of getting the current task from the main coroutin
import asyncio

#define a main coroutine
async def main():
    #report a message
    print('main coroutine started')
    #get the current task
    task = asyncio.current_task()
    #report its details
    print(task)
#start the asyncio progarm
asyncio.run(main())