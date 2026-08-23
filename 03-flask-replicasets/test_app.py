import unittest
from app import app
class TestSale(unittest.TestCase):
    def test_home(self):
        self.assertEqual(app.test_client().get("/").status_code,200)
    def test_buy(self):
        self.assertEqual(app.test_client().get("/buy?user=student").json["user"],"student")
if __name__=="__main__":
    unittest.main()
