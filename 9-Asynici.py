import asyncio
import time
# define and asynchronous itertoor
class StopAsyncIteratoy():
    #constuructor,define some state
    def _init_(self):
        self.counter = 0 