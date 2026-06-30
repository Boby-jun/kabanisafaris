import os, http.server, socketserver

os.chdir(os.path.dirname(os.path.abspath(__file__)))
PORT = 4321
with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()
