import unittest
from app import app
class TestFlask(unittest.TestCase):
    def test_home(self):
        self.assertEqual(app.test_client().get("/").status_code,200)
    def test_health(self):
        self.assertEqual(app.test_client().get("/health").json["status"],"healthy")
if __name__=="__main__":
    unittest.main()
