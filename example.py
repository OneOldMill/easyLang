# Python 3 server example
# https://pythonbasics.org/webserver/
from http.server import BaseHTTPRequestHandler, HTTPServer
#import time
#import db_select.py
from process import input_process

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
     def do_GET(self):
        self.send_response(200)
        #self.send_response(status.code, status.message)
        #self.send_header("Content-type", "text/html")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>GET: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is do_GET of HTTP server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
        self.wfile.close()
        #self.wfile.write(bytes("Hello, world!", "utf-8"))

     def do_POST(self):
        # read the content-length header
        content_length = int(self.headers.get("Content-Length"))
        # read that many bytes from the body of the request
        body = self.rfile.read(content_length)

        result = input_process(body)

        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        #self.wfile.write(body)
        self.wfile.write(bytes(result, 'utf8'))
    
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")