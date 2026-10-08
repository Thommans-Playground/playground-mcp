from typing import Annotated

from mcp.server.mcpserver import MCPServer
from mcp.types import ToolAnnotations
from pydantic import Field

from hello_world.application.ports import GreetingPort
from hello_world.application.services import GreetingService


def create_server(greeting_port: GreetingPort | None = None) -> MCPServer:
    port = greeting_port or GreetingService()
    server = MCPServer("hello-world")

    @server.tool(
        annotations=ToolAnnotations(
            title="Greet a person",
            read_only_hint=True,
            destructive_hint=False,
            idempotent_hint=True,
            open_world_hint=False,
        )
    )
    def greet(
        name: Annotated[
            str,
            Field(description="The person's name to greet. Must be non-empty."),
        ],
    ) -> str:
        """Return a friendly greeting for the given name.

        Raises an error if name is empty or only whitespace.
        """
        return port.greet(name).message

    return server
