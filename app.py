"""Prefect Horizon deployment entrypoint for Splitwise MCP Server.

Horizon expects a module-level FastMCP instance. This file creates one
and exposes it as `mcp` for the entrypoint config: app.py:mcp
"""

from splitwise_mcp_server.server import create_server

mcp = create_server()
