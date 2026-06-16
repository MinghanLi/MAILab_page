from __future__ import annotations

import argparse
import http.server
import socketserver
from pathlib import Path


ROOT = Path(__file__).resolve().parent


class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


def serve(port: int) -> None:
    handler = http.server.SimpleHTTPRequestHandler

    with ReusableTCPServer(("", port), handler) as httpd:
        print(f"Serving MAI Lab site at http://127.0.0.1:{port}")
        print("Press Ctrl+C to stop.")
        httpd.serve_forever()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Local preview server for the MAI Lab static site."
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to serve the site on. Default: 8000",
    )
    args = parser.parse_args()

    # Serve the repo root so GitHub Pages-compatible files resolve directly.
    import os

    os.chdir(ROOT)
    serve(args.port)


if __name__ == "__main__":
    main()
