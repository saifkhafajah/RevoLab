import http.server
import socketserver
import webbrowser
import os
import sys
import threading
import time

PORT = 8000
FILE_NAME = "index.html"

def start_server():
    class Handler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, format, *args):
            pass 

    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"\n[INFO] RevoLab running at http://localhost:{PORT}")
            print("[INFO] Press Ctrl+C to stop.\n")
            httpd.serve_forever()
    except OSError:
        print(f"[ERROR] Port {PORT} is busy.")
        os._exit(1)

if __name__ == "__main__":
    if not os.path.exists(FILE_NAME):
        print(f"[ERROR] '{FILE_NAME}' not found.")
        sys.exit(1)

    threading.Thread(target=start_server, daemon=True).start()
    time.sleep(1)
    webbrowser.open(f"http://localhost:{PORT}/{FILE_NAME}")

    try:
        while True: time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(0)
