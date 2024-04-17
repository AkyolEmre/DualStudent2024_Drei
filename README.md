# Customer Data Management with Flask and SQLite

This project provides functionality to manage and serve customer data using a Flask web application and SQLite database. It consists of two main parts:

1. **API to Serve Customer Data**
2. **Script to Populate Database from CSV**



## Installation

1. Clone this repository:

   ```bash
   https://github.com/AkyolEmre/DualStudent2024_Drei.git
   ```

2. Install the required dependencies:

   ```bash
   pip install Flask
   ```

3. Ensure SQLite is installed on your system. If not, download and install it from the SQLite website.



## Usage

### 1. API to Serve Customer Data

- Start the Flask application by running `app.py`:

  ```bash
  python app.py
  ```

- Access the following endpoints:
  - `http://localhost:5000/`: Home page with basic HTML interface.
  - `http://localhost:5000/get_customers`: Endpoint to retrieve customer data in JSON format.

### 2. Script to Populate Database from CSV

- Run the Python script `populate_database.py` to populate the database with customer data from a CSV file:

  ```
  python populate_database.py
  ```



## Configuration

- By default, the application uses an SQLite database named `customer_data.db` located in the project directory. You can modify the database path or name by changing the corresponding value in the `app.py` and `populate_database.py` files.



### Index.html

1. Open the `index.html` file in a web browser to access the customer data management interface.
2. Interact with the following features:
   - **Search**: Use the search input box to filter customers by their information.
   - **Sort by Name**: Click the "Sort by Name" button to sort customers alphabetically by their first names.
   - **Filter Options**: Choose from various filter options to display customers based on specific criteria.



## Test Cases

### 1. Search Functionality

- **Test Case 1**: Entering a customer's name should display only that customer's information.
- **Test Case 2**: Entering a partial name should display all customers whose names contain the entered text.

### 2. Sort by Name

- **Test Case 1**: Clicking the "Sort by Name" button once should sort customers alphabetically by their first names in ascending order.
- **Test Case 2**: Clicking the "Sort by Name" button twice should reverse the sorting order to descending.

### 3. Filter Options

- **Test Case 1**: Selecting "All Customers" from the filter options should display all customers.
- **Test Case 2**: Selecting "2021" from the filter options should display only customers who subscribed in 2021.
- **Test Case 3**: Selecting "2022" from the filter options should display only customers who subscribed in 2022.



## File Structure

```
├── app.py
├── populate_database.py
├── customer_data.db
├── customer_sales_2021_2022.csv
├── templates/
│   └── index.html
└── README.md
```