import docker

client = docker.from_env()
container = client.containers.run(
    "secure-flask",
    detach=True,
    security_opt=["apparmor=secure-flask"],
)
try:
    info = client.api.inspect_container(container.id)
    print("Applied profile:", info.get("AppArmorProfile"))
    for command in [
        ["python", "-c", "open('/etc/shadow').read()"],
        ["/bin/sh", "-c", "cat /etc/shadow"],
    ]:
        result = container.exec_run(command)
        print("Command:", command)
        print("Exit code:", result.exit_code)
        print(result.output.decode(errors="replace"))
finally:
    container.stop()
    container.remove()
