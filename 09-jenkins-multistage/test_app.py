import unittest
from app import app
class TestApp(unittest.TestCase):
    def test_home(self):
        r = app.test_client().get("/")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.get_data(as_text=True), "Hello, Jenkins Multi-Stage Pipeline!")
if __name__ == "__main__":
    unittest.main()
