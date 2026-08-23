# Experiment 3: Scale a Flask Application using ReplicaSets

**Date:** 23 August 2026

## Aim
To study and implement scale a flask application using replicasets.

## Requirements
Docker, Minikube and kubectl.

## Program / Configuration Files
`app.py`, `Dockerfile`, `requirements.txt`, `test_app.py`, `replicaset.yaml`, `service.yaml`

The complete source code and configuration files are included alongside this record. Open the linked files in this directory to view the implementation.

## Procedure
1. Build the Flask image from the repository root: `minikube image build -t devops-flask:1.0 03-flask-replicasets`.
2. Apply `replicaset.yaml` and `service.yaml`.
3. Inspect `kubectl get rs,pods -l app=flask-rs`.
4. Scale up: `kubectl scale rs/flask-rs --replicas=5`.
5. Verify five Pods using `kubectl get pods -l app=flask-rs`.
6. Scale down: `kubectl scale rs/flask-rs --replicas=2`.
7. Delete a Pod and check that the ReplicaSet replaces it.
8. Open the service with `minikube service flask-rs`. Test `/buy?user=student` to see a simulated purchase response.

## Expected Output
ReplicaSet maintains the desired Pod count when scaling or when a Pod is removed.

## Result
The experiment demonstrates scale a flask application using replicasets using the supplied code and commands.

## Reference
[Instructor's Exercise 3](https://github.com/SunagP/DevOps-Lab/tree/main/Exercises)
