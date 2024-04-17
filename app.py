from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_customers')
def get_customers():
    conn = sqlite3.connect('customer_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customers')
    columns = [column[0] for column in cursor.description]
    customers = [dict(zip(columns, row)) for row in cursor.fetchall()]
    conn.close()
    return jsonify(customers)

if __name__ == '__main__':
    app.run(debug=True)
