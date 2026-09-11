import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread

from app.hermes_health import probe_hermes


def test_probe_empty_url_is_not_configured() -> None:
    assert probe_hermes("") == "not_configured"


def test_probe_unreachable_local_port() -> None:
    assert probe_hermes("http://127.0.0.1:1", timeout=0.2) == "unreachable"


def test_probe_get_302_is_serve_ui() -> None:
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            self.send_response(302)
            self.send_header("Location", "/login")
            self.end_headers()

        def do_HEAD(self) -> None:
            self.send_response(302)
            self.send_header("Location", "/login")
            self.end_headers()

        def log_message(self, *_args: object) -> None:
            return

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        host, port = server.server_address
        assert probe_hermes(f"http://{host}:{port}", timeout=0.4) == "serve_ui"
    finally:
        server.shutdown()
        server.server_close()


def test_probe_head_405_means_reachable() -> None:
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            time.sleep(2)

        def do_HEAD(self) -> None:
            self.send_response(405)
            self.send_header("Allow", "GET")
            self.end_headers()

        def log_message(self, *_args: object) -> None:
            return

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        host, port = server.server_address
        assert probe_hermes(f"http://{host}:{port}", timeout=0.4) == "reachable"
    finally:
        server.shutdown()
        server.server_close()