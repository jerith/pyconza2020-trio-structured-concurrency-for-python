import trio

async def print_lines(msg, n):
    for i in range(n):
        print(i+1, msg)
        await trio.sleep(0.2)
    print("task finished:", msg)

async def main():
    print("parent: started!")
    async with trio.open_nursery() as nursery:
        nursery.start_soon(print_lines, "task1", 4)
        nursery.start_soon(print_lines, "task2", 2)
        print("parent: waiting for tasks to finish...")
    print("parent: all done!")

trio.run(main)
