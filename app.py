"""Prefect Horizon deployment entrypoint for Splitwise MCP Server.

Horizon expects a module-level FastMCP instance. This file creates one
and exposes it as `mcp` for the entrypoint config: app.py:mcp
"""
import os
import uvicorn
from splitwise_mcp_server.server import create_server
from starlette.applications import Starlette
from starlette.routing import Mount

mcp = create_server()

# Get the ASGI app from FastMCP but strip any auth/OAuth middleware
app = mcp.http_app(path="/mcp")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
