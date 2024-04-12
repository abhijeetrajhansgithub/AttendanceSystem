import sqlite3
import time
import secrets
DATABASE = "B:\Computer Science and Engineering\PycharmIDE\ManipalAttendanceProjectV1\Database\database.db"


def delete_from_database():
    try:
        database = DATABASE
        table_name = "one_time_password"
        # Connect to the SQLite database
        connection = sqlite3.connect(database)

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Delete all records from the specified table
        cursor.execute(f"DELETE FROM {table_name};")

        # Commit the changes and close the connection
        connection.commit()
        connection.close()

        print(f"All records deleted from {table_name} successfully.")

    except sqlite3.Error as error:
        print(f"Error deleting records: {error}")


def generate_one_time_password():
    # Generate a secure random 9-digit number
    otp = secrets.randbelow(10**9)
    # Format the number as a 9-digit string (with leading zeros if needed)
    otp_string = f"{otp:09d}"
    return otp_string


def insert_into_database(otp):
    try:
        database = DATABASE
        table_name = "one_time_password"
        # Connect to the SQLite database
        connection = sqlite3.connect(database)

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Insert the OTP into the specified table
        cursor.execute(f"INSERT INTO {table_name} VALUES (?)", (otp,))

        # Commit the changes and close the connection
        connection.commit()
        connection.close()

        print(f"OTP {otp} inserted into {table_name} successfully.")

    except sqlite3.Error as error:
        print(f"Error inserting OTP: {error}")


def change_otp_in_database():
    while True:
        delete_from_database()
        otp_generated = generate_one_time_password()
        insert_into_database(otp_generated)
        print("OTP: ", retrieve_otp())
        time.sleep(10)




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

        # Commit the changes and close the connection
        connection.commit()
        connection.close()

        return otp

    except sqlite3.Error as error:
        print(f"Error retrieving OTP: {error}")
        return None


def run_server_database():
    change_otp_in_database()


if __name__ == '__main__':
    run_server_database()
