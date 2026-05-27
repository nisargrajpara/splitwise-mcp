"""Prefect Horizon deployment entrypoint for Splitwise MCP Server.

Horizon expects a module-level FastMCP instance. This file creates one
and exposes it as `mcp` for the entrypoint config: app.py:mcp
"""
import os
from splitwise_mcp_server.server import create_server
from fastmcp import FastMCP

mcp = create_server()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=port,
        stateless_http=True
    )
