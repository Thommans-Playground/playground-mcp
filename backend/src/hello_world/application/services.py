from hello_world.application.ports import GreetingPort
from hello_world.domain.greeting import Greeting


class GreetingService(GreetingPort):
    def greet(self, name: str) -> Greeting:
        return Greeting.for_recipient(name)
