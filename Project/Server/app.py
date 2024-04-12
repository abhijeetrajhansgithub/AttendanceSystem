import secrets

from flask import Flask, render_template
import threading
import time
import sqlite3

DATABASE = rf"B:\Computer Science and Engineering\PycharmIDE\ManipalAttendanceProjectV1\Database\database.db"

app = Flask(__name__)


def retrieve_otp():
    try:
        database = DATABASE
        table_name = "one_time_password"
        # Connect to the SQLite database
        connection = sqlite3.connect(database)

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Retrieve the OTP from the specified table
        cursor.execute(f"SELECT otp FROM {table_name};")
        otp = cursor.fetchone()[0]

        # Close the connection
        connection.close()

        return otp

    except sqlite3.Error as error:
        print(f"Error retrieving OTP: {error}")
        return None


@app.route('/', methods=['GET', 'POST'])
def run():

    while True:
        time.sleep(2)
        one_time_password = retrieve_otp()

        return render_template('server.html', otp=one_time_password)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
