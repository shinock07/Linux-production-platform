from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)


class LinuxOpsHandler(BaseHTTPRequestHandler):

    def send_json(self, status_code, response):

        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        self.wfile.write(
            json.dumps(response).encode()
        )

    def do_GET(self):

        logging.info(
            "GET %s from %s",
            self.path,
            self.client_address[0]
        )

        if self.path == "/":

            response = {
                "service": "Linux Production Platform",
                "status": "running"
            }

            self.send_json(200, response)

        elif self.path == "/health":

            response = {
                "status": "healthy"
            }

            self.send_json(200, response)

        elif self.path == "/status":

            response = {
                "service": "Linux Production Platform",
                "status": "running",
                "version": "0.1.0"
            }

            self.send_json(200, response)

        else:

            response = {
                "error": "Not Found"
            }

            self.send_json(404, response)


server = HTTPServer(
    ("127.0.0.1", 8000),
    LinuxOpsHandler
)

logging.info(
    "Linux Production Platform starting on port 8000"
)

server.serve_forever()
