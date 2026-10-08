import uvicorn

from hello_world.adapters.rest import create_app

app = create_app()


def main() -> None:
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
