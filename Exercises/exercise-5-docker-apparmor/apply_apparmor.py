
import docker

client = docker.from_env()
container = None

try:
    print("Building Docker image...")

    image, logs = client.images.build(
        path=".",
        tag="flask-apparmor"
    )

    print("Docker image built successfully!")

    print("Starting container with AppArmor profile...")

    container = client.containers.run(
        "flask-apparmor",
        ports={"5000/tcp": 5000},
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True
    )

    print("Container started:", container.short_id)

    container.reload()

    info = container.attrs
    security_options = info["HostConfig"]["SecurityOpt"]

    print("Applied security options:", security_options)

    if "apparmor=my-apparmor-profile" in (security_options or []):
        print("AppArmor profile configured successfully.")
    else:
        print("AppArmor profile was not found in security options.")

finally:
    if container is not None:
        print("Stopping container...")
        container.stop()
        container.remove()
        print("Container stopped and removed.")
