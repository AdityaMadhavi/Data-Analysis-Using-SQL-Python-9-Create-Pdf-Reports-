import sqlite3
import random
import datetime

# Define SQL commands for creating the tables
create_sales_table = '''CREATE TABLE Sales (
                        sale_id INTEGER PRIMARY KEY,
                        Sale_date DATE,
                        customer_id INTEGER,
                        product_id INTEGER,
                        quantity INTEGER,
                        unit_price DECIMAL(10,2),
                        total_price DECIMAL(10,2),
                        FOREIGN KEY (customer_id) REFERENCES customers(Customer_id),
                        FOREIGN KEY (product_id) REFERENCES products(product_id),
                        )'''

create_products_table = '''CREATE TABLE products (
                        product_id INTEGER PRIMARY KEY,
                        product_name TEXT,
                        unit_cost Decimal(10,2)
                        )'''

create_customers_table = '''CREATE TABLE customers (
                        customer_id INTEGER PRIMARY KEY,
                        first_name TEXT,
                        last_name TEXT,
                        email TEXT,
                        phone TEXT,
                        )'''

# Sql commands for inserting the sample data into Tables
insert_products_data = '''INSERT INTO products (product_name,unit_cost) VALUES (?,?)'''

insert_sales_data = '''INSERT INTO sales (sales_date,customer_id,product_id,quantity,unit_price,total_price) VALUES (?,?,?,?,?,?)'''

insert_customers_data = '''INSERT INTO customers (first_name,last_name,email,phone) VALUES (?,?,?,?)'''

# Define sample data for the products and customer tables
products = [('Product A', 50.00), ('Product B', 25.00),
            ('Product c', 75.00), ('Product D', 40.00), ('Product E', 60.00)]

customers = [
    ('Aditya', 'Madhavi', 'adimadha1212@gmail.com', '121-1212'),
    ('Rush', 'Sap', 'rushsap212@gmail.com', '122-1213'),
    ('Hit', 'ASs', 'hitas@gmail.com', '125-1222'),
    ('Jude', 'Roy', 'JudeRoy312@gmail.com', '111-1412'),
    ('Sujoy', 'Updhaya', 'suadpad@gmail.com', '221-1212'),
    ('Shubha', 'Jeet', 'Sujeet212@gmail.com', '421-1243'),
    ('Ravi', 'Pakya', 'rpraka@gmail.com', '431-2121'),
    ('Rahul', 'Singh', 'rsingh@gmail.com', '811-1212')
]
# Define the start and end dates for generating sales data
start_date = datetime.date(2022, 1, 1)
end_date = datetime.date(2022, 12, 31)

# connect to the database and create the tables
with sqlite3.connect('sales.db') as conn:
    # create the sales Table
    # conn.execute(create_sales_table)

    # create the products table
    # conn.execute(create_products_table)

    # create the customer table
    # conn.execute(create_customers_table)

    # Insert Sample data into the products table
    for product in products:
        conn.execute(insert_products_data, product)

    # Insert Sample data into the customers table
    for customer in customers:
        conn.execute(insert_customers_data, customer)

    # Insert sample data into the sales table
    for i in range(1000):
        sale_date = start_date + \
            datetime.timedelta(days=random.randint(0, 364))
        customer_id = random.randint(1, len(customers))
        product_id = random.randint(1, len(products))
        quantity = random.randint(1, 10),
        unit_price = products[product_id-1][1]
        total_price = quantity * int(unit_price)
        conn.execute(insert_sales_data, (sale_date, customer_id,
                     product_id, quantity, unit_price, total_price))

# commit changes
    conn.commit()

    print("Database successfully created!")
