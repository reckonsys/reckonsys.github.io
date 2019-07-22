import asyncio


async def handle(reader, writer):
    body = b'{"foo": "bar"}\r\n'
    writer.write(b'HTTP/1.1 200 OK\r\n')
    writer.write(b'Content-Type: application/json\r\n')
    writer.write(b'Content-Length: %d' % len(body))
    writer.write(b'\r\n\r\n')
    writer.write(body)
    writer.write(b'\r\n\r\n')
    # await writer.drain()
    # writer.close()
    # await writer.wait_closed()


async def main():
    server = await asyncio.start_server(handle, '127.0.0.1', 8888)

    async with server:
        await server.serve_forever()

asyncio.run(main())
