# Experiment 7: Continuous Integration with Jenkins

**Date:** 20 September 2026

## Aim
To study and implement continuous integration with jenkins.

## Requirements
Jenkins, Git, Python 3.

## Program / Configuration Files
`Dockerfile`, `plugins.txt`, `compose.yaml`, `Jenkinsfile`

The complete source code and configuration files are included alongside this record. Open the linked files in this directory to view the implementation.

## Procedure
1. Run `docker compose up --build -d` to start Jenkins and open `http://localhost:8080`. Obtain the initial admin password using `docker compose exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword`.
2. Create a Pipeline job named `devops-ci-lab`.
3. Choose Pipeline script from SCM and Git as the SCM.
4. Enter this repository URL and use branch `main`.
5. Set Script Path to `07-jenkins-ci/Jenkinsfile`.
6. Save and click Build Now.
7. Open Console Output to inspect checkout and Python syntax validation stages.

## Expected Output
Jenkins checks out the Git repository and validates Python source syntax.

## Result
The experiment demonstrates continuous integration with jenkins using the supplied code and commands.

## Reference
[Instructor's Exercise 7](https://github.com/SunagP/DevOps-Lab/tree/main/Exercises)
