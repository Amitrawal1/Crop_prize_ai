from app.services.agmarknet.client import AgmarknetClient


def main() -> None:
    client = AgmarknetClient()

    filters = client.get_filters()

    print(filters["data"].keys())


if __name__ == "__main__":
    main()