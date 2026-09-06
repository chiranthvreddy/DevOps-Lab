import docker
client=docker.from_env()
container=client.containers.run("secure-flask",detach=True,ports={"5000/tcp":5000},security_opt=["apparmor=secure-flask"],remove=True)
try:
    print("Container:",container.short_id)
    print("AppArmor:",client.api.inspect_container(container.id)["HostConfig"]["SecurityOpt"])
    input("Press Enter to stop...")
finally:
    container.stop()
