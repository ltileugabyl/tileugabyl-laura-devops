import os
from http.server import BaseHTTPRequestHandler, HTTPServer


def banner():
    line = "=" * 32
    return "\n".join([
        line,
        "DevOps Student Application",
        line,
        "",
        "Name: " + os.getenv("STUDENT_NAME", "Laura"),
        "Surname: " + os.getenv("STUDENT_SURNAME", "Tileugabyl"),
        "Group: " + os.getenv("STUDENT_GROUP", "IT2-2311"),
        "Student ID: " + os.getenv("STUDENT_ID", "41586"),
        "",
        "Application is running successfully!",
    ])


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = banner().encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    print(banner(), flush=True)
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
