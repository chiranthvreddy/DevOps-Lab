# Experiment 10: Multi-Node Kubernetes Deployment

**Date:** 11 October 2026

## Aim
To study and implement multi-node kubernetes deployment.

## Requirements
Docker, Minikube, kubectl and enough memory for three nodes.

## Program / Configuration Files
`catalog.py`, `cart.py`, `Dockerfile`, `requirements.txt`, `apps.yaml`

The complete source code and configuration files are included alongside this record. Open the linked files in this directory to view the implementation.

## Procedure
1. Start a three-node cluster: `minikube start -p devops-multinode --nodes 3 --driver=docker`.
2. From this folder build both images: `docker build -t devops-catalog:1.0 --build-arg APP_FILE=catalog.py .` and `docker build -t devops-cart:1.0 --build-arg APP_FILE=cart.py .`.
3. Load both images using `minikube -p devops-multinode image load devops-catalog:1.0` and similarly for `devops-cart:1.0`.
4. Apply `apps.yaml`: `kubectl --context devops-multinode apply -f apps.yaml`.
5. Inspect nodes and Pod placement with `kubectl --context devops-multinode get nodes` and `kubectl --context devops-multinode get pods -o wide`.
6. Confirm two catalog replicas and three cart replicas.
7. Access each app using `minikube -p devops-multinode service catalog` and `minikube -p devops-multinode service cart`.

## Expected Output
Catalog and cart deployments run with two and three replicas respectively across the Minikube cluster.

## Result
The experiment demonstrates multi-node kubernetes deployment using the supplied code and commands.

## Reference
[Instructor's Exercise 10](https://github.com/SunagP/DevOps-Lab/tree/main/Exercises)
