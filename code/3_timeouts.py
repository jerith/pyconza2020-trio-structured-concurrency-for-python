import trio

async def main():
    with trio.move_on_after(3):
        print("Went to sleep")
        await trio.sleep(2)
        print("Still sleeping")
        await trio.sleep(2)
        print("Woke up on my own")
    print("Nap time is over")

    try:
        with trio.fail_after(2):
            async with open_nursery() as n:
                n.start_soon(trio.sleep, 1)
                n.start_soon(trio.sleep, 3)
                await trio.sleep(4)
    except trio.TooSlowError as e:
        print(f"Took too long: {e!r}")

trio.run(main)
