from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
import json
import argparse
import platform


class Model:

    def __init__(self) -> None:
        self.users = {
            "kostas":"myman",
            "takis":"noman",
            "andrew":"dend"
        }
    
    def get_users(self):
        return json.dumps(self.users)
        

def controller(model):
    class GetHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed_path = parse.urlparse(self.path)
            real_path = parsed_path.path
            if real_path == "/users":
                message = model.get_users()
            else:
                message = '''
                <html> 
                <body>
                <h2>OK RUNNING</h2>
                </body>
                </html>

                '''
            self.send_response(200)
            self.send_header('Content-Type', 'text/html;charset=utf-8')
            self.end_headers()
            self.wfile.write(message.encode('utf-8'))
    return GetHandler


def main(hostname, port):
    server = HTTPServer((hostname, port), controller(Model()))
    print(f"Node info: {platform.node()}")
    print(f"Starting server listening on: {hostname}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("hostname", help="Hostname")
    parser.add_argument("port", help="Port to listen to")
    args = vars(parser.parse_args())
    main(args["hostname"], int(args["port"]))
