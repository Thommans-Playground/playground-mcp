from fastapi import FastAPI

from hello_world.application.ports import GreetingPort
from hello_world.application.services import GreetingService


def create_app(greeting_port: GreetingPort | None = None) -> FastAPI:
    port = greeting_port or GreetingService()
    app = FastAPI(title="Hello World API")

    @app.get("/greet/{name}")
    def greet(name: str) -> dict[str, str]:
        greeting = port.greet(name)
        return {"recipient": greeting.recipient, "message": greeting.message}

    return app
