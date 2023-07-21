#example of an asynchronous context manager via async with
import asyncio 
import time 

import asyncio

#define an  asynchronous context manager
class AasynchronousManager:
    #enter the async context manager 
    async def __aenter__(self):
    #reoport a message 
        print(f'{time.ctime()} >entering the context manager')
    #block for a moment
        await asyncio.sleep(0.5)

    #exit the async context manager
    async def __aexit__(self, exc_type, exc, tb):
        #port a message
        print(f'{time.ctime()} >extiting the context manager')
        #block for a  moment
        await asyncio.sleep(0.5)

    #define a simple coroutine
async def custom_coroutine():
    #creata and use the asynchronous context manager
    async with AasynchronousManager() as manager:
        #report the resulet
            print(f'{time.ctime()} within the manager')

#start the asycio progeam
asyncio.run(custom_coroutine())    


# Wed Jul 19 14:53:34 2023 >entering the context manager
# Wed Jul 19 14:53:34 2023 within the manager
# Wed Jul 19 14:53:34 2023 >extiting the context manager

