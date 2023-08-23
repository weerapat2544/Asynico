from random import random
import asyncio
import time

# coroutine to generate work


async def producer(queqe,id):
    print(f'{time.ctime()} Producer {id}: Running')
    # generate work
    for i in range(10):
        # generate work
        value = random()
        # block to simulate work
        await asyncio.sleep(id*0.1)
        # add to the queqe
        await queqe.put(value)
    print(f'{time.ctime()} Producer {id}: Done')


async def consumer(queqe):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit for work
        item = await queqe.get()
        # report
        print(f'{time.ctime()} >got {item}')
        # block while processing
        if item:
            await asyncio.sleep(item)
        # mark as completed
        queqe.task_done()
    # all done
    print(f'{time.ctime()} Consumer: Done')

# entry point coroutine


async def main():
    # create the shared queqe
    queue = asyncio.Queue(2)
    # start the consumer
    _ = asyncio.create_task(consumer(queue))
    # create many product
    product = [producer(queue,_) for _ in range(5)]
    # run and wait for the producers to finish
    await asyncio.gather(*product)
    # wait for the consumer to process all item
    await queue.join()
# start the asyncio program
asyncio.run(main())
# Wed Aug 23 15:28:42 2023 Consumer: Running
# Wed Aug 23 15:28:42 2023 Producer 0: Running
# Wed Aug 23 15:28:42 2023 Producer 1: Running
# Wed Aug 23 15:28:42 2023 Producer 2: Running
# Wed Aug 23 15:28:42 2023 Producer 3: Running
# Wed Aug 23 15:28:42 2023 Producer 4: Running
# Wed Aug 23 15:28:42 2023 >got 0.3435107748042322
# Wed Aug 23 15:28:42 2023 >got 0.46514336978011683
# Wed Aug 23 15:28:43 2023 >got 0.5706215384012645
# Wed Aug 23 15:28:43 2023 >got 0.011556700782460294
# Wed Aug 23 15:28:43 2023 >got 0.7436486110106092
# Wed Aug 23 15:28:44 2023 >got 0.4244441240472828
# Wed Aug 23 15:28:44 2023 >got 0.5935789686503778
# Wed Aug 23 15:28:45 2023 >got 0.6043654275110908
# Wed Aug 23 15:28:46 2023 >got 0.4555330044980994
# Wed Aug 23 15:28:46 2023 >got 0.5076560495461345
# Wed Aug 23 15:28:47 2023 >got 0.5190526896509405
# Wed Aug 23 15:28:47 2023 >got 0.7213772505225983
# Wed Aug 23 15:28:48 2023 >got 0.022027239327712667
# Wed Aug 23 15:28:48 2023 >got 0.0965326834425656
# Wed Aug 23 15:28:48 2023 >got 0.05822012495549689
# Wed Aug 23 15:28:48 2023 >got 0.15828810097171409
# Wed Aug 23 15:28:48 2023 >got 0.9972485111322856
# Wed Aug 23 15:28:49 2023 >got 0.26042612500887563
# Wed Aug 23 15:28:50 2023 >got 0.49037090884490653
# Wed Aug 23 15:28:50 2023 >got 0.8752595043418149
# Wed Aug 23 15:28:51 2023 >got 0.002142686455934073
# Wed Aug 23 15:28:51 2023 >got 0.6543574356482599
# Wed Aug 23 15:28:52 2023 >got 0.5020041106223325
# Wed Aug 23 15:28:52 2023 >got 0.7049753628167347
# Wed Aug 23 15:28:53 2023 >got 0.8044727540390958
# Wed Aug 23 15:28:54 2023 >got 0.7922828138010948
# Wed Aug 23 15:28:54 2023 >got 0.5698806082982879
# Wed Aug 23 15:28:55 2023 >got 0.4409085708484525
# Wed Aug 23 15:28:55 2023 >got 0.9026368082772823
# Wed Aug 23 15:28:55 2023 Producer 0: Done
# Wed Aug 23 15:28:56 2023 >got 0.5463547475666493
# Wed Aug 23 15:28:57 2023 >got 0.9434095794037116
# Wed Aug 23 15:28:58 2023 >got 0.7259541652311684
# Wed Aug 23 15:28:59 2023 >got 0.09899815336423945
# Wed Aug 23 15:28:59 2023 >got 0.444215337055231
# Wed Aug 23 15:28:59 2023 >got 0.0758193285951907
# Wed Aug 23 15:28:59 2023 >got 0.9921501270270812
# Wed Aug 23 15:29:00 2023 >got 0.6533317383528507
# Wed Aug 23 15:29:01 2023 >got 0.2556032622526271
# Wed Aug 23 15:29:01 2023 >got 0.3038220560517618
# Wed Aug 23 15:29:02 2023 >got 0.821240857610299
# Wed Aug 23 15:29:02 2023 >got 0.39379029704365354
# Wed Aug 23 15:29:03 2023 >got 0.5998324163044105
# Wed Aug 23 15:29:03 2023 Producer 1: Done
# Wed Aug 23 15:29:03 2023 >got 0.9111847397584178
# Wed Aug 23 15:29:04 2023 >got 0.215951261406377
# Wed Aug 23 15:29:05 2023 >got 0.9831555938428866
# Wed Aug 23 15:29:06 2023 >got 0.5188759112399588
# Wed Aug 23 15:29:06 2023 Producer 3: Done
# Wed Aug 23 15:29:06 2023 >got 0.9546444597512126
# Wed Aug 23 15:29:06 2023 Producer 4: Done
# Wed Aug 23 15:29:07 2023 >got 0.6016130388063947
# Wed Aug 23 15:29:07 2023 Producer 2: Done
# Wed Aug 23 15:29:08 2023 >got 0.32446274795766916
# Wed Aug 23 15:29:08 2023 >got 0.29752805045010056