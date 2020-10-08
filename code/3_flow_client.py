async def client_send_and_receive(client_stream, data):
    while True:
        print(f"sender: sending {data!r}")
        await client_stream.send_all(data)
        received = await client_stream.receive_some()
        print(f"receiver: got data {received!r}")
        if not received:
            print("receiver: connection closed")
            sys.exit()
        await trio.sleep(1)
