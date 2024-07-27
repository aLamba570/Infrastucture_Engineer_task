from data_processor import OrderProcessor

def main():
    # Path to the CSV file
    file_path = 'orders.csv'
    
    # Create an instance of OrderProcessor
    processor = OrderProcessor(file_path)
    
    # Compute total revenue per month
    monthly_revenue = processor.total_revenue_per_month()
    print("Total Revenue per Month:")
    print(monthly_revenue)
    print("\n")

    # Compute total revenue per product
    product_revenue = processor.total_revenue_per_product()
    print("Total Revenue per Product:")
    print(product_revenue)
    print("\n")

    # Compute total revenue per customer
    customer_revenue = processor.total_revenue_per_customer()
    print("Total Revenue per Customer:")
    print(customer_revenue)
    print("\n")

    # Identify top 10 customers by revenue
    top_customers = processor.top_customers_by_revenue()
    print("Top 10 Customers by Revenue:")
    print(top_customers)

if __name__ == "__main__":
    main()
