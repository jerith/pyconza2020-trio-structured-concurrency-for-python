import asyncio

async def raise_error(msg):
    await asyncio.sleep(0.1)
    raise Exception(msg)

async def main():
    t1 = asyncio.create_task(raise_error("task1"))  # Never awaited.
    t2 = asyncio.create_task(raise_error("task2"))  # Awaited later.
    await asyncio.create_task(raise_error("task3"))  # Awaited now.
    await t2

asyncio.run(main())
