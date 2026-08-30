# Experiment 4: Docker Networking with Flask, MySQL and Redis

**Lab date:** 30 August 2026

## Aim
Create a user-defined bridge network connecting Flask, MySQL and Redis. Verify container-name DNS and access the Flask API.

## Files
`app.py`, `requirements.txt`, `Dockerfile`, `compose.yaml`, `test_app.py`.

## Steps
1. Install Docker Engine / Docker Desktop with Compose.
2. Open a terminal in `04-docker-networking`.
3. Set the database password: Git Bash: `export MYSQL_ROOT_PASSWORD='choose-a-password'`; PowerShell: `$env:MYSQL_ROOT_PASSWORD='choose-a-password'`.
4. Run `docker compose up --build -d`. Compose creates the bridge network `devops-lab-bridge` and starts all three containers.
5. Verify with `docker compose ps`, `docker network ls`, and `docker network inspect devops-lab-bridge`.
6. Verify service discovery from Flask: `docker compose exec web python -c 'import socket; print(socket.gethostbyname("mysql")); print(socket.gethostbyname("redis"))'`.
7. Open `http://localhost:5001/about`. The API returns its name, version and description.
8. Optional unit test on a Python environment with Flask installed: `python -m unittest test_app.py`.
9. Stop containers and remove the network with `docker compose down`.

## Result
The Flask, MySQL and Redis containers share a user-defined bridge network and resolve each other by service name.

## Reference
[Instructor's Exercise 4](https://github.com/SunagP/DevOps-Lab/blob/main/Exercises/4-Docker-Networking.md)
