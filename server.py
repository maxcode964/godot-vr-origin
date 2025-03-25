from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add the required headers for Godot HTML5
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        super().end_headers()

# Start the server on port 8000 (or any other port you prefer)
with TCPServer(("", 8000), CORSRequestHandler) as httpd:
    print("Serving at http://localhost:8000")
    httpd.serve_forever()