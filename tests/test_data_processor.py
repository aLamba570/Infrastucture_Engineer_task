import unittest
import pandas as pd
from app.data_processor import OrderProcessor

class TestOrderProcessor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        data = {
            'order_id': [1, 2, 3, 4],
            'customer_id': [101, 102, 101, 103],
            'order_date': pd.to_datetime(['2024-01-01', '2024-01-15', '2024-02-10', '2024-02-25']),
            'product_id': [501, 502, 501, 503],
            'product_name': ['Product A', 'Product B', 'Product A', 'Product C'],
            'product_price': [20, 30, 20, 50],
            'quantity': [2, 1, 1, 3]
        }
        cls.processor = OrderProcessor(pd.DataFrame(data))

    def test_total_revenue_per_month(self):
        expected = pd.DataFrame({'month': ['2024-01', '2024-02'], 'product_price': [50, 70]})
        result = self.processor.total_revenue_per_month()
        pd.testing.assert_frame_equal(result, expected)

    def test_total_revenue_per_product(self):
        expected = pd.DataFrame({'product_name': ['Product A', 'Product B', 'Product C'], 'product_price': [40, 30, 50]})
        result = self.processor.total_revenue_per_product()
        pd.testing.assert_frame_equal(result, expected)

    def test_total_revenue_per_customer(self):
        expected = pd.DataFrame({'customer_id': [101, 102, 103], 'product_price': [40, 30, 50]})
        result = self.processor.total_revenue_per_customer()
        pd.testing.assert_frame_equal(result, expected)

    def test_top_customers_by_revenue(self):
        expected = pd.DataFrame({'customer_id': [103, 101], 'product_price': [50, 40]})
        result = self.processor.top_customers_by_revenue(top_n=2)
        pd.testing.assert_frame_equal(result, expected)

if __name__ == '__main__':
    unittest.main()
