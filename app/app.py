import os
import psycopg2
from http.server import BaseHTTPRequestHandler, HTTPServer

def check_db():
    try:
        conn = psycopg2.connect(
            host=os.environ.get("DB_HOST"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            dbname=os.environ.get("DB_NAME")
        )
        conn.close()
        return "DB OK"
    except Exception as e:
        return f"DB ERROR: {e}"

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        db_status = check_db()
        self.wfile.write(f"Hello DevOps\n{db_status}".encode())

server = HTTPServer(("0.0.0.0", 8000), Handler)
server.serve_forevers()