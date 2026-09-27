# Experiment 8: Jenkins Hello World Job

**Date:** 27 September 2026

## Aim
To study and implement jenkins hello world job.

## Requirements
Jenkins and Git.

## Program / Configuration Files
`Jenkinsfile`, `hello-world.sh`

The complete source code and configuration files are included alongside this record. Open the linked files in this directory to view the implementation.

## Procedure
1. Create a new Jenkins Pipeline job named `hello-world`.
2. Select Pipeline script from SCM and configure the repository and `main` branch.
3. Set Script Path to `08-jenkins-hello-world/Jenkinsfile`.
4. Build the job and open Console Output.
5. Inspect the Hello World stage and the message `Hello, Jenkins!`.
6. The pipeline executes the shell script stored in `hello-world.sh`.

## Expected Output
The Jenkins console displays `Hello, Jenkins!` from the shell script.

## Result
The experiment demonstrates jenkins hello world job using the supplied code and commands.

## Reference
[Instructor's Exercise 8](https://github.com/SunagP/DevOps-Lab/tree/main/Exercises)
