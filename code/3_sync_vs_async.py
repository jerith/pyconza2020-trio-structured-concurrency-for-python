import trio

def square(n):
    return n * n

async def cube(n):
    return n * square(n)

trio.run(cube, 2)
