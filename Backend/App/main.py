from services.agmarknet.client import AgmarknetClient


def main():
    client = AgmarknetClient()

    filters = client.get_filters()

    print(filters.keys())


if __name__ == "__main__":
    main()