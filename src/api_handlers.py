import json

class ApiHandler:

    def load_request_body(self, server):
        length = int(server.headers.get("Content-length"))
        body = json.loads(
            server.rfile
                .read(length)
                .decode("utf-8")
        )
        print("TEXT ----- :   ", body["text"])
        return body