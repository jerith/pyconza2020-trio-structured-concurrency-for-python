import trio

async def echo_server(server_stream):
    conn_id = id(server_stream)
    print(f"echo_server {conn_id}: started")
    try:
        async for data in server_stream:
            print(f"echo_server {conn_id}: received data {data!r}")
            await server_stream.send_all(data)
        print(f"echo_server {conn_id}: connection closed")
    except Exception as exc:
        print(f"echo_server {conn_id}: crashed: {exc!r}")

async def main():
    await trio.serve_tcp(echo_server, 12345)

trio.run(main)
