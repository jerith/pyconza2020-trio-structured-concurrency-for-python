import trio

async def print_lines(msg, n):
    for i in range(n):
        print(i+1, msg)
        await trio.sleep(0.4)

async def timebomb(delay):
    await trio.sleep(delay)
    raise Exception("KABOOOM!")

async def main():
    try:
        async with trio.open_nursery() as n:
            n.start_soon(print_lines, "child", 5)
            n.start_soon(timebomb, 1)
            await print_lines("body", 5)
    except Exception as e:
        print(f"Error: {e}")

trio.run(main)
