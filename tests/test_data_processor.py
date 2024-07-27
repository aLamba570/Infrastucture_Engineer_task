import sys
import os
import unittest
import pandas as pd

# Add the parent directory of app to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

from data_processor import OrderProcessor

class TestOrderProcessor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Sample data to mimic the structure of your CSV
        data = {
            'order_id': [1, 2, 3],
            'order_date': ['2024-01-01', '2024-01-02', '2024-01-03'],
            'amount': [100, 150, 200]
        }
        
        # Create a DataFrame and save it to a CSV file for testing
        cls.test_csv_path = os.path.join(os.path.dirname(__file__), 'test_orders.csv')
        pd.DataFrame(data).to_csv(cls.test_csv_path, index=False)
        
        # Initialize the OrderProcessor with the test CSV path
        cls.processor = OrderProcessor(cls.test_csv_path)

    @classmethod
    def tearDownClass(cls):
        # Clean up the test CSV file
        os.remove(cls.test_csv_path)

    def test_order_processor_initialization(self):
        self.assertIsNotNone(self.processor.df)

if __name__ == '__main__':
    unittest.main()
