from http.server import HTTPServer, SimpleHTTPRequestHandler
from socketserver import ThreadingMixIn
import os

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        super().end_headers()

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass

PORT = 8000
Handler = CORSRequestHandler

httpd = ThreadedHTTPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()
