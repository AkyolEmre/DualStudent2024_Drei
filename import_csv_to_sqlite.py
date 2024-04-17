import sqlite3
import csv

# Connect to SQLite database
conn = sqlite3.connect('customer_data.db')
cursor = conn.cursor()

# Create table to store customer data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        customer_id TEXT,
        first_name TEXT,
        last_name TEXT,
        company TEXT,
        city TEXT,
        country TEXT,
        phone1 TEXT,
        phone2 TEXT,
        email TEXT,
        subscription_date TEXT,
        website TEXT,
        sales_2021 REAL,
        sales_2022 REAL
    )
''')

# Read CSV file and insert data into the database
with open('customer_sales_2021_2022.csv', 'r', newline='') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        customer_id = row['Customer Id']
        first_name = row['First Name']
        last_name = row['Last Name']
        company = row['Company']
        city = row['City']
        country = row['Country']
        phone1 = row['Phone 1']
        phone2 = row['Phone 2']
        email = row['Email']
        subscription_date = row['Subscription Date']
        website = row['Website']
        sales_2021 = float(row['SALES 2021'])
        sales_2022 = float(row['SALES 2022'])

        cursor.execute('''
            INSERT INTO customers (customer_id, first_name, last_name, company, city, country, phone1, phone2, email, subscription_date, website, sales_2021, sales_2022)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (customer_id, first_name, last_name, company, city, country, phone1, phone2, email, subscription_date, website, sales_2021, sales_2022))

conn.commit()
conn.close()
