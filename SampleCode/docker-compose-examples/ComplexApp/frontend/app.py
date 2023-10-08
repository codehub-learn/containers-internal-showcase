######################################################################
# @author      : Kostas Makedos (kostas.makedos@gmail.com)
# @file        : backend
# @created     : Παρασκευή Μαρ 10, 2023 00:40:09 EET
# @copyright   : Copyright (c) Makedos GP, 2023
######################################################################


from http.server import BaseHTTPRequestHandler
from urllib import parse, request

class GETHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = parse.urlparse(self.path)
        req_path = parsed_path.path
        print(req_path)
#        response = request.urlopen("http://complexapp_backend_1:8000/" + req_path)
#        message = "Response: " + response.read()
        message = "Empty"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))


if __name__ == "__main__":
    from http.server import HTTPServer
    server = HTTPServer(('0.0.0.0', 8000), GETHandler)
    print("Frontend starting to serve at 0.0.0.0:8000")
    server.serve_forever()

