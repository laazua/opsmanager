from app import start_server


def main() -> None:
    server, port = start_server()
    print(f"Server Start On [:{port}]")
    try:
        server.wait_for_termination()
    except KeyboardInterrupt as e:
        pass


if __name__ == "__main__":
    main()
