# Experiment 5: Docker Security with AppArmor

**Lab date:** 6 September 2026

## Aim
Restrict a containerized Flask application with a custom AppArmor profile and test denied file access.

## Requirements
Linux/Ubuntu with Docker, AppArmor and Python Docker SDK. AppArmor enforcement cannot be demonstrated on Windows containers.

## Files
`app.py`, `Dockerfile`, `secure-flask.profile`, `apply_apparmor.py`, `test_restricted_actions.py`.

## Steps
1. Check AppArmor: `sudo aa-status`. Install tools if needed: `sudo apt install apparmor-utils`.
2. Load the policy from this directory: `sudo apparmor_parser -r secure-flask.profile`.
3. Build the container: `docker build -t secure-flask .`.
4. Install the Python SDK on the host: `python3 -m pip install docker` (use a virtual environment if required).
5. Apply the policy through Docker SDK: `python3 apply_apparmor.py`. Verify the printed security option, then press Enter to stop the container.
6. Run `python3 test_restricted_actions.py` to start a new confined container, inspect its applied profile, and attempt restricted reads and command execution.
7. Check the exit codes, permission-denied output and AppArmor audit logs. Exit codes depend on runtime and profile enforcement.
8. Optionally run the container directly: `docker run --rm --security-opt apparmor=secure-flask -p 5000:5000 secure-flask`.

## Expected Result
The `secure-flask` AppArmor profile confines the container and denies reads of `/etc/shadow`. The test script checks the applied profile and reports the results of restricted access attempts.

## Reference
[Instructor's Exercise 5](https://github.com/SunagP/DevOps-Lab/blob/main/Exercises/5-Docker-Security-AppArmor.md)
