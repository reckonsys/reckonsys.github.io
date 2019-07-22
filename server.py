from http.server import BaseHTTPRequestHandler
from socketserver import TCPServer


class SimpleHTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"foo": "bar"}')


with TCPServer(('', 9090), SimpleHTTPHandler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

httpd.server_close()
