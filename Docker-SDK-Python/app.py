import docker 
from docker.errors import NotFound, APIError

client = docker.from_env()


def list_containers():
    containers = client.containers.list(all=True)

    if not containers:
        print("\nNo containers found.\n")
        return

    print("\nContainers:")
    print("-" * 50)
    for c in containers:
        print(f"Name: {c.name}")
        print(f"Image: {c.image.tags}")
        print(f"Status: {c.status}")
        print("-" * 50)


def run_container():
    image = input("Image name: ")
    name = input("Container name (leave blank for auto): ")

    try:
        kwargs = {
            "image": image,
            "detach": True
        }

        if name:
            kwargs["name"] = name

        if image == "ubuntu":
            kwargs["command"] = "sleep 300"

        container = client.containers.run(**kwargs)

        print(f"\nContainer '{container.name}' started.\n")

    except APIError as e:
        print(e)


def stop_container():
    name = input("Container name: ")

    try:
        container = client.containers.get(name)
        container.stop()
        print("Container stopped.")

    except NotFound:
        print("Container not found.")


def start_container():
    name = input("Container name: ")

    try:
        container = client.containers.get(name)
        container.start()
        print("Container started.")

    except NotFound:
        print("Container not found.")


def restart_container():
    name = input("Container name: ")

    try:
        container = client.containers.get(name)
        container.restart()
        print("Container restarted.")

    except NotFound:
        print("Container not found.")


def remove_container():
    name = input("Container name: ")

    try:
        container = client.containers.get(name)
        container.remove(force=True)
        print("Container removed.")

    except NotFound:
        print("Container not found.")


def show_logs():
    name = input("Container name: ")

    try:
        container = client.containers.get(name)
        print(container.logs().decode())

    except NotFound:
        print("Container not found.")


def execute_command():
    name = input("Container name: ")
    command = input("Command: ")

    try:
        container = client.containers.get(name)
        result = container.exec_run(command)
        print(result.output.decode())

    except NotFound:
        print("Container not found.")


def inspect_container():
    name = input("Container name: ")

    try:
        container = client.containers.get(name)

        print("\nContainer Details")
        print("-----------------")
        print("ID:", container.short_id)
        print("Name:", container.name)
        print("Status:", container.status)
        print("Image:", container.image.tags)
        print("Created:", container.attrs["Created"])

    except NotFound:
        print("Container not found.")


def container_stats():
    name = input("Container name: ")

    try:
        container = client.containers.get(name)

        stats = container.stats(stream=False)

        print("\nMemory Usage:")
        print(stats["memory_stats"]["usage"], "bytes")

    except NotFound:
        print("Container not found.")


def list_images():
    images = client.images.list()

    print()

    for image in images:
        if image.tags:
            print(image.tags)
        else:
            print(image.short_id)


def pull_image():
    image = input("Image name: ")

    client.images.pull(image)

    print("Image downloaded.")


def remove_image():
    image = input("Image name: ")

    try:
        client.images.remove(image)
        print("Image removed.")

    except APIError as e:
        print(e)


def build_image():
    path = input("Dockerfile directory (.): ") or "."
    tag = input("Image tag: ")

    try:
        client.images.build(path=path, tag=tag)
        print("Image built successfully.")

    except APIError as e:
        print(e)


while True:

    print("""
========== Docker Manager ==========
1. List Containers
2. Run Container
3. Stop Container
4. Start Container
5. Restart Container
6. Remove Container
7. Show Logs
8. Execute Command
9. Inspect Container
10. Container Statistics
11. List Images
12. Pull Image
13. Remove Image
14. Build Image
15. Exit
""")

    choice = input("Enter choice: ")

    if choice == "1":
        list_containers()

    elif choice == "2":
        run_container()

    elif choice == "3":
        stop_container()

    elif choice == "4":
        start_container()

    elif choice == "5":
        restart_container()

    elif choice == "6":
        remove_container()

    elif choice == "7":
        show_logs()

    elif choice == "8":
        execute_command()

    elif choice == "9":
        inspect_container()

    elif choice == "10":
        container_stats()

    elif choice == "11":
        list_images()

    elif choice == "12":
        pull_image()

    elif choice == "13":
        remove_image()

    elif choice == "14":
        build_image()

    elif choice == "15":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
