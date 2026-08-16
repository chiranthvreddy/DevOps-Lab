# Experiment 2: Deploy a Flask App using Minikube and kubectl

**Date:** 16 August 2026

## Aim
To study and implement deploy a flask app using minikube and kubectl.

## Requirements
Docker, Minikube, kubectl, Python and Flask.

## Program / Configuration Files
`app.py`, `Dockerfile`, `requirements.txt`, `test_app.py`, `deployment.yaml`, `service.yaml`

The complete source code and configuration files are included alongside this record. Open the linked files in this directory to view the implementation.

## Procedure
1. Start Minikube with `minikube start`.
2. Build the Flask image from the repository root: `minikube image build -t devops-flask:1.0 02-minikube-flask`.
3. From this lab folder apply both manifests: `kubectl apply -f deployment.yaml -f service.yaml`.
4. Check readiness with `kubectl rollout status deployment/flask-app`.
5. Inspect Pods using `kubectl get pods -l app=flask-app`.
6. Access the Flask API using `minikube service flask-app`.

## Expected Output
The Flask endpoint responds with a welcome message; `/health` returns a healthy status.

## Result
The experiment demonstrates deploy a flask app using minikube and kubectl using the supplied code and commands.

## Reference
[Instructor's Exercise 2](https://github.com/SunagP/DevOps-Lab/tree/main/Exercises)
