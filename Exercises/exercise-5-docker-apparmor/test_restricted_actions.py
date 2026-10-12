
import docker

client = docker.from_env()
container = None

try:
    print("Starting container with AppArmor profile...")

    container = client.containers.run(
        "flask-apparmor",
        command="python -c \"import time; time.sleep(60)\"",
        detach=True,
        security_opt=["apparmor=my-apparmor-profile"],
    )

    print("Container started successfully.")

    tests = [
        ("Read /etc/passwd", ["cat", "/etc/passwd"]),
        ("Execute /bin/sh", ["/bin/sh", "-c", "echo shell-executed"]),
    ]

    for description, command in tests:
        print(f"\nTesting: {description}")

        try:
            result = container.exec_run(command)
            output = result.output.decode(errors="replace").strip()

            print(f"Exit code: {result.exit_code}")
            print(f"Output: {output or '(no output)'}")

            if result.exit_code != 0:
                print("RESULT: Command blocked or failed.")
            else:
                print("RESULT: Command succeeded.")

        except docker.errors.APIError as error:
            print(f"RESULT: Command failed: {error}")

    print("\nAll tests completed.")

finally:
    if container is not None:
        try:
            container.stop()
        except docker.errors.DockerException:
            pass

        try:
            container.remove()
        except docker.errors.DockerException:
            pass
