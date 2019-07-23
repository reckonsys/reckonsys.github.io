import asyncio


class AsyncHTTPHandler:
    '''
    This is just to mimic the socketserver.TCPServer functionality
    '''
    def __init__(self, writer):
        self.wfile = writer

    def send_response(self, status):
        self.wfile.write(f'HTTP/1.1 {status} OK\r\n'.encode())

    def send_header(self, header, value):
        self.wfile.write(f'{header}: {value}\r\n'.encode())

    def end_headers(self):
        self.wfile.write(b'\r\n\r\n')

    def do_GET(self):
        body = b'{"foo": "bar"}'
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', len(body))
        self.end_headers()
        self.wfile.write(body)

    async def end_response(self):
        await self.wfile.drain()
        self.wfile.close()
        await self.wfile.wait_closed()


async def handle(reader, writer):
    handler = AsyncHTTPHandler(writer)
    handler.do_GET()
    await handler.end_response()


async def main():
    server = await asyncio.start_server(handle, '0.0.0.0', 8888)

    async with server:
        await server.serve_forever()

asyncio.run(main())
