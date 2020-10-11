import asyncio

async def print_lines(msg, n):
    for i in range(n):
        print(i+1, msg)
        await asyncio.sleep(0.2)

async def main():
    await print_lines("basically sync", 3)
    t1 = asyncio.create_task(print_lines("task1", 3))
    t2 = asyncio.create_task(print_lines("task2", 6))
    await t1
    await t2

asyncio.run(main())
