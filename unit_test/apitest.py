import requests
import unittest

class unitTestAPI(unittest.TestCase):
    def test_api_200(self):
        url = "http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7.json?api-key=4GKINutELZVWbAcMVVmJmJDV2rhxWYbh"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, dict)
        self.assertIn("results", data)
        print("\nTest 200 ok !")

    def test_api_404(self):
        url = "http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/njj.json?api-key=4GKINutELZVWbAcMVVmJmJDV2rhxWYbh"
        response = requests.get(url)
        self.assertEqual(response.status_code, 404)
        print("\nTest 404 ok !")

    def test_err_apikey(self):
        url = "http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7.json?api-key=wrong-key"
        response = requests.get(url)
        self.assertEqual(response.status_code, 401)
        data = response.json()
        self.assertIsInstance(data, dict)
        print("\nTest 401 ok !")