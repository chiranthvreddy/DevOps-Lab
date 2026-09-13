import random
import time
from prometheus_client import Counter, Gauge, start_http_server
completed = Counter("delivery_completed_total", "Completed deliveries")
pending = Gauge("delivery_pending", "Pending deliveries")
latency = Gauge("delivery_latency_seconds", "Delivery duration")
if __name__ == "__main__":
    start_http_server(8000)
    while True:
        completed.inc(random.randint(0, 4))
        pending.set(random.randint(0, 40))
        latency.set(random.uniform(5, 45))
        time.sleep(5)
