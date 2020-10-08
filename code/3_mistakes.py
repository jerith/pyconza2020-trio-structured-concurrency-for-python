import trio

async def slow_square(n):
    await trio.sleep(0.2)
    return n * n

def foo():
    print(await slow_square(3))  # SyntaxError

async def bar():
    print(slow_square(3))  # RuntimeWarning logged
