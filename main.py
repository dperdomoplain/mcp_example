from mcp.server.fastmcp import FastMCP

from stack_overflow_mcp.tools.tools import (
    get_last_post_with_activity,
    get_most_viewed_posts,
)

server = FastMCP(
    "Stack Overflow MCP Server",
    version="1.0.0",
    description="A server for Stack Overflow MCP tools",
    host="0.0.0.0",
    port=8000,
)


server.add_tool(
    name="get_most_viewed_posts",
    description="Get the most viewed posts from Stack Overflow database",
    fn=get_most_viewed_posts,
)

server.add_tool(
    name="get_last_post_with_activity",
    description="Get the last post with activity from Stack Overflow database",
    fn=get_last_post_with_activity,
)


if __name__ == "__main__":
    server.run("streamable-http")
