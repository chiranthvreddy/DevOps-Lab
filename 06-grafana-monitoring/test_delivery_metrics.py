import unittest
from prometheus_client import REGISTRY
import delivery_metrics
class MetricsTest(unittest.TestCase):
    def test_metrics_registered(self):
        names={item.name for item in REGISTRY.collect()}
        self.assertIn("delivery_pending",names)
        self.assertIn("delivery_completed",names)
if __name__=="__main__":
    unittest.main()
