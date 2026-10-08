from dataclasses import dataclass


@dataclass(frozen=True)
class Greeting:
    recipient: str
    message: str

    @classmethod
    def for_recipient(cls, recipient: str) -> "Greeting":
        name = recipient.strip()
        if not name:
            raise ValueError("recipient must not be empty")
        return cls(recipient=name, message=f"Hello, {name}!")
