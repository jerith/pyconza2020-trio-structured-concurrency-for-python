import asyncio

async def print_lines(msg, n):
    for i in range(n):
        print(i+1, msg)
        await asyncio.sleep(0.2)

async def main():
    await print_lines("basically sync", 3)
    t0 = print_lines("task0", 3)  # Coroutine created but not run.
    t1 = asyncio.create_task(print_lines("task1", 3))
    t2 = asyncio.create_task(print_lines("task2", 6))
    await t1
    # We forgot to await t2, so we might exit before it finishes.

asyncio.run(main())
