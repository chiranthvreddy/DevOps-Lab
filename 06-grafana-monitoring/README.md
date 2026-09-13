# Experiment 6: Real-Time Delivery Monitoring with Prometheus, Grafana and Jenkins

**Lab date:** 13 September 2026

## Aim
Simulate delivery operations, expose Prometheus metrics, visualize a Grafana dashboard, and define alerts.

## Files
`delivery_metrics.py`, `test_delivery_metrics.py`, `Dockerfile`, `requirements.txt`, `prometheus.yml`, `alerts.yml`, `grafana-datasource.yml`, `grafana-dashboard-provider.yml`, `grafana-dashboard.json`, `compose.yaml`, `Jenkinsfile`.

## Steps
1. Open a terminal in `06-grafana-monitoring` and run `docker compose up --build -d`.
2. Inspect simulated metrics at `http://localhost:8000/metrics` including `delivery_pending`, `delivery_completed_total` and `delivery_latency_seconds`.
3. Open Prometheus at `http://localhost:9090`; query the three metrics and inspect the Alerts page.
4. Open Grafana at `http://localhost:3000`, sign in, and change the default password. The Prometheus datasource and **Delivery Operations Monitoring** dashboard are provisioned automatically.
5. Inspect the dashboard panels for pending deliveries, completed deliveries and delivery latency.
6. Inspect the two alert rules: `TooManyPendingDeliveries` (pending >10 for 15s) and `HighAverageDeliveryTime` (sampled latency >30s for 15s).
7. The `Jenkinsfile` supplies a separate automation demonstration; configure Jenkins to run it if required.
8. Shut down with `docker compose down`.

## Expected Result
The exporter is scraped by Prometheus, the dashboard visualizes the data, and alert states change when thresholds persist.

## Reference
[Instructor's Exercise 6](https://github.com/SunagP/DevOps-Lab/blob/main/Exercises/6-Grafana-Realtime-Monitoring-of-Quick-Commerce-App.md)
