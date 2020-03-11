import unittest
from app import app

class TestProbleem(unittest.TestCase):


    def setUp(self) -> None:
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        self.app = app.test_client()

    def tearDown(self) -> None:
        pass

    def test_probemie(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 500)


if __name__ == '__main__':
    unittest.main()