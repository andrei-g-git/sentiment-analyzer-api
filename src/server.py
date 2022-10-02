from http.server import HTTPServer, BaseHTTPRequestHandler

class AnalyzerServer(BaseHTTPRequestHandler):
    def do_POST(self):
        print("awefaew")

    def do_GET(self):
        self.handle_post_headers("/test")
        print("prepare to send response")
        self.wfile.write(bytes("request received", "utf8"))

    def handle_post_headers(self, path):
        self.send_response(200)
        self.path = path
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header("Content-type", "application/json")
        self.end_headers()

    @staticmethod
    def init_server(HOST, PORT):
        server = HTTPServer((HOST, PORT), AnalyzerServer) #so this passes it's class before it can fully instantiate? ...
        print("server running at ", HOST, " ", PORT)
        server.serve_forever()
        server.server_close()
        print("server stopped...")
        
        return "Server running at ", HOST, "  on port ", PORT           