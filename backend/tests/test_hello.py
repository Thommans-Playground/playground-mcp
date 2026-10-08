import pytest
from fastapi.testclient import TestClient

from hello_world.adapters.rest import create_app
from hello_world.application.services import GreetingService
from hello_world.domain.greeting import Greeting


def test_greeting_domain_builds_message():
    greeting = Greeting.for_recipient("Ada")
    assert greeting.message == "Hello, Ada!"


def test_greeting_domain_rejects_blank_name():
    with pytest.raises(ValueError):
        Greeting.for_recipient("   ")


def test_service_delegates_to_domain():
    service = GreetingService()
    greeting = service.greet("Grace")
    assert greeting.message == "Hello, Grace!"


def test_rest_adapter_returns_greeting():
    client = TestClient(create_app())
    response = client.get("/greet/Linus")
    assert response.status_code == 200
    assert response.json() == {"recipient": "Linus", "message": "Hello, Linus!"}
