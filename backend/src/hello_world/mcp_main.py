from hello_world.adapters.mcp import create_server

server = create_server()


def main() -> None:
    server.run()


if __name__ == "__main__":
    main()
