# Experiment 1: Deploy an Nginx Pod in Kubernetes

**Date:** 09 August 2026

## Aim
To study and implement deploy an nginx pod in kubernetes.

## Requirements
Docker, Minikube, kubectl.

## Program / Configuration Files
`pod.yaml`, `service.yaml`

The complete source code and configuration files are included alongside this record. Open the linked files in this directory to view the implementation.

## Procedure
1. Start Minikube: `minikube start`.
2. Create an Nginx Pod with `kubectl apply -f pod.yaml`.
3. Create the NodePort Service using `kubectl apply -f service.yaml`.
4. Inspect resources with `kubectl get pods -o wide` and `kubectl get svc`.
5. Open the page using `minikube service hello-k8s`.
6. Describe the Pod using `kubectl describe pod hello-k8s`.

## Expected Output
The Nginx welcome page is displayed through the NodePort service, and the Pod is Running.

## Result
The experiment demonstrates deploy an nginx pod in kubernetes using the supplied code and commands.

## Reference
[Instructor's Exercise 1](https://github.com/SunagP/DevOps-Lab/tree/main/Exercises)
