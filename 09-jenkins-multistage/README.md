# Experiment 9: Jenkins Multi-Stage Pipeline

**Lab date:** 4 October 2026

## Aim
Build, test, deploy, run and check a Flask application using Jenkins.

## Files
`app.py`, `test_app.py`, `requirements.txt`, `Jenkinsfile`.

## Steps
1. Ensure the Jenkins Linux agent has Python 3 and the `python3-venv` package.
2. In Jenkins create a Pipeline job, select **Pipeline script from SCM**, choose Git and enter this repository URL and the `main` branch.
3. Set Script Path to `09-jenkins-multistage/Jenkinsfile`.
4. Click **Build Now**.
5. The **Build** stage creates a virtual environment and installs requirements.
6. The **Test** stage runs the Flask unit test.
7. The **Deploy** stage copies application files into `deployed-app`.
8. **Run Application** launches Flask; **Test Application** retries an HTTP request to verify it responds.
9. The post-build step stops the background process and archives the deployed files.
10. Review the Jenkins Console Output for stage results and the archived deployment artifacts.

## Expected Result
A successful pipeline executes all stages and returns HTTP 200 from the deployed Flask app.

## Reference
[Instructor's Exercise 9](https://github.com/SunagP/DevOps-Lab/blob/main/Exercises/9-Jenkins-Multi-Stage-Pipeline.md)
