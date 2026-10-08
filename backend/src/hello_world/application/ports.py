from typing import Protocol

from hello_world.domain.greeting import Greeting


class GreetingPort(Protocol):
    def greet(self, name: str) -> Greeting: ...
