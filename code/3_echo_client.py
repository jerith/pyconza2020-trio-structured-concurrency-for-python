import sys
import trio

async def sender(client_stream, data):
    while True:
        print(f"sender: sending {data!r}")
        await client_stream.send_all(data)
        await trio.sleep(1)

async def receiver(client_stream):
    async for data in client_stream:
        print(f"receiver: got data {data!r}")
    print("receiver: connection closed")
    sys.exit()

async def main(argv):
    data = (argv + ["default message"])[1].encode("utf-8")
    client_stream = await trio.open_tcp_stream("127.0.0.1", 12345)
    async with client_stream:
        async with trio.open_nursery() as nursery:
            nursery.start_soon(sender, client_stream, data)
            nursery.start_soon(receiver, client_stream)

trio.run(main, sys.argv)
