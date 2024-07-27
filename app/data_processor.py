import pandas as pd

class OrderProcessor:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path, parse_dates=['order_date'])

    def total_revenue_per_month(self):
        # Use .dt to access datetime properties
        self.df['month'] = self.df['order_date'].dt.to_period('M')
        monthly_revenue = self.df.groupby('month')['product_price'].sum().reset_index()
        return monthly_revenue

    def total_revenue_per_product(self):
        product_revenue = self.df.groupby('product_name')['product_price'].sum().reset_index()
        return product_revenue

    def total_revenue_per_customer(self):
        customer_revenue = self.df.groupby('customer_id')['product_price'].sum().reset_index()
        return customer_revenue

    def top_customers_by_revenue(self, top_n=10):
        customer_revenue = self.total_revenue_per_customer()
        top_customers = customer_revenue.nlargest(top_n, 'product_price')
        return top_customers

if __name__ == "__main__":
    processor = OrderProcessor('orders.csv')
    print("Total Revenue per Month:")
    print(processor.total_revenue_per_month())
    print("\nTotal Revenue per Product:")
    print(processor.total_revenue_per_product())
    print("\nTotal Revenue per Customer:")
    print(processor.total_revenue_per_customer())
    print("\nTop 10 Customers by Revenue:")
    print(processor.top_customers_by_revenue())
