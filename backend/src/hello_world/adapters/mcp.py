from mcp.server.mcpserver import MCPServer

from hello_world.application.ports import GreetingPort
from hello_world.application.services import GreetingService


def create_server(greeting_port: GreetingPort | None = None) -> MCPServer:
    port = greeting_port or GreetingService()
    server = MCPServer("hello-world")

    @server.tool()
    def greet(name: str) -> str:
        """Greet a person by name."""
        return port.greet(name).message

    return server
