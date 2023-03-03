import time
import asyncio
async def function():
    await asyncio.sleep(1)
    print("print 1")


async def function1():
    await asyncio.sleep(1)
    print("print 2")


async def function2():
    await asyncio.sleep(4)

    print("print 3")

async def main():
    task = asyncio.create_task(function1())
    await function()
    # await function1()
    await function2()

asyncio.run(main())