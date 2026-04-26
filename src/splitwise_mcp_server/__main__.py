"""Entry point for the Splitwise MCP Server."""

import asyncio
import os
import sys
from splitwise_mcp_server.server import create_server


def main():
    """Main entry point for the MCP server.

    Supports two transports:
    - stdio (default): For local MCP clients like Claude Desktop
    - http: For remote hosting on Prefect Horizon
      Set FASTMCP_TRANSPORT=http or pass --http flag
    """
    try:
        server = create_server()

        use_http = (
            os.environ.get("FASTMCP_TRANSPORT", "").lower() == "http"
            or "--http" in sys.argv
        )

        if use_http:
            host = os.environ.get("FASTMCP_HOST", "0.0.0.0")
            port = int(os.environ.get("FASTMCP_PORT", "8000"))
            asyncio.run(server.run(transport="http", host=host, port=port))
        else:
            asyncio.run(server.run())
    except KeyboardInterrupt:
        print("\nShutting down Splitwise MCP Server...")
        sys.exit(0)
    except Exception as e:
        print(f"Error starting server: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
