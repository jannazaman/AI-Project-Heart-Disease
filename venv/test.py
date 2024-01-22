import unittest
from app import app

class TestHeartDiseasePrediction(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()

        # Create input features for testing
        self.form_data = {
            'Age': '45',
            'Sex': '1',
            'CP': '2',
            'fbs': '0',
            'trestbps': '140',
            'Chol': '200',
            'exang': '0'
        }

    def test_predict_disease_route(self):
        # Send a POST request to the /Predict_disease route with form data
        response = self.app.post('/Predict_disease', data=self.form_data)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the result is present in the response
        self.assertIn(b'Result:', response.data)


if __name__ == '__main__':
    unittest.main()
