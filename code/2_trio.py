import trio

async def print_lines(msg, n):
    for i in range(n):
        print(i+1, msg)
        await trio.sleep(0.2)

async def main():
    await print_lines("basically sync", 3)

    async with trio.open_nursery() as n:
        n.start_soon(print_lines, "task1", 3)
        n.start_soon(print_lines, "task2", 6)

trio.run(main)
