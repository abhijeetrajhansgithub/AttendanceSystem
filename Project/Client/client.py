from flask import Flask, render_template, jsonify, request, url_for, redirect
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

DATABASE = rf"B:\Computer Science and Engineering\PycharmIDE\ManipalAttendanceProjectV1\Database\database.db"

app = Flask(__name__, static_folder='static', template_folder='templates')


def insert_into_database(email, password):
    try:
        database = DATABASE
        table_name = "users"
        # Connect to the SQLite database
        connection = sqlite3.connect(database)

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Insert the email and password into the specified table
        cursor.execute(f"INSERT INTO {table_name} VALUES (?, ?)", (email, password))

        # Commit the changes and close the connection
        connection.commit()
        connection.close()

        print(f"User {email} inserted into {table_name} successfully.")

    except sqlite3.Error as error:
        print(f"Error inserting user: {error}")


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


@app.route('/')
def login_page():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Add your authentication logic here
        if authenticate_user(email, password):
            return redirect(url_for('user_profile', username=email))
        else:
            return jsonify({'status': 'error', 'message': 'Invalid credentials'})


@app.route('/open-signup', methods=['POST'])
def open_signup():
    # Redirect to the signup page
    return redirect(url_for('signup'))


# Add a route for the signup page
@app.route('/signup')
def signup():
    return render_template('signup.html')


def authenticate_user(email, password):
    print(password)
    if email and password:
        try:
            table_name = "users"
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM {table_name} WHERE email = ? AND password = ?", (email, password))
            user = cur.fetchone()
            conn.close()

            if user:
                return True
            else:
                return False

        except sqlite3.Error as error:
            print(f"Error authenticating user: {error}")
            return False


@app.route('/user_profile')
def user_profile():
    username = request.args.get('username')
    return render_template('user_profile.html', username=username)


@app.route('/create-new-account', methods=['POST'])
def create_new_account():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']

        if password != confirm_password:
            return jsonify({'status': 'error', 'message': 'Passwords do not match'})
        else:
            insert_into_database(email, password)
            return redirect(url_for('login_page'))


def check_iteration(username):
    try:
        database = DATABASE
        table_name = "check_otps_entered"
        # Connect to the SQLite database
        connection = sqlite3.connect(database)

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Retrieve the OTP from the specified table
        cursor.execute(f"SELECT iteration FROM {table_name} WHERE email = ?;", (username,))
        iteration = cursor.fetchone()[0]

        # Close the connection
        connection.close()

        return iteration

    except sqlite3.Error as error:
        print(f"Error retrieving OTP: {error}")
        return None


def if_iteration_is_none(username, generated_otp, entered_otp):
    try:
        database = DATABASE
        table_name = "check_otps_entered"
        # Connect to the SQLite database
        connection = sqlite3.connect(database)

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Insert into database values email and iteration set to 1 and enter f01 and fu1 and put others as Null
        cursor.execute(f"INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                       (username, 1, generated_otp, entered_otp, None, None, None, None, None, None, None, None))

        # Commit the changes and close the connection
        connection.commit()

        # Close the connection
        connection.close()

    except sqlite3.Error as error:
        print(f"Error retrieving OTP: {error}")
        return None


def get_iteration(username):
    try:
        database = DATABASE
        table_name = "check_otps_entered"
        # Connect to the SQLite database
        connection = sqlite3.connect(database)

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Retrieve the OTP from the specified table
        cursor.execute(f"SELECT iteration FROM {table_name} WHERE email = ?;", (username,))
        iteration = cursor.fetchone()[0]

        # Close the connection
        connection.close()

        return iteration

    except sqlite3.Error as error:
        print(f"Error retrieving OTP: {error}")
        return None


def enter_other_entered_otps(username, generated_otp, entered_otp, match=True):
    try:
        database = DATABASE
        table_name = "check_otps_entered"
        # Connect to the SQLite database
        connection = sqlite3.connect(database)

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Get iteration
        iteration = get_iteration(username)
        if iteration is None:
            return
        elif iteration == 1 and match is True:
            # update iteration, fo2 and fu2
            cursor.execute(f"UPDATE {table_name} SET iteration = ?, fo2 = ?, fu2 = ? WHERE email = ?;", (iteration + 1, generated_otp, entered_otp, username))
        elif iteration == 1 and match is False:
            # update iteration, fo1 and fu1
            cursor.execute(f"UPDATE {table_name} SET iteration = ?, fo1 = ?, fu1 = ? WHERE email = ?;", (iteration + 1, generated_otp, "False", username))
        elif iteration == 2 and match is True:
            # update iteration, fo3 and fu3
            cursor.execute(f"UPDATE {table_name} SET iteration = ?, fo3 = ?, fu3 = ? WHERE email = ?;", (iteration + 1, generated_otp, entered_otp, username))
        elif iteration == 2 and match is False:
            # update iteration, fo3 and fu3
            cursor.execute(f"UPDATE {table_name} SET iteration = ?, fo3 = ?, fu3 = ? WHERE email = ?;", (iteration + 1, generated_otp, "False", username))
        elif iteration == 3 and match is True:
            # update iteration, fo4 and fu4
            cursor.execute(f"UPDATE {table_name} SET iteration = ?, fo4 = ?, fu4 = ? WHERE email = ?;", (iteration + 1, generated_otp, entered_otp, username))
        elif iteration == 3 and match is False:
            # update iteration, fo4 and fu4
            cursor.execute(f"UPDATE {table_name} SET iteration = ?, fo4 = ?, fu4 = ? WHERE email = ?;", (iteration + 1, generated_otp, "False", username))
        elif iteration == 4 and match is True:
            # update iteration, fo5 and fu5
            cursor.execute(f"UPDATE {table_name} SET iteration = ?, fo5 = ?, fu5 = ? WHERE email = ?;", (iteration + 1, generated_otp, entered_otp, username))
        elif iteration == 4 and match is False:
            # update iteration, fo5 and fu5
            cursor.execute(f"UPDATE {table_name} SET iteration = ?, fo5 = ?, fu5 = ? WHERE email = ?;", (iteration + 1, generated_otp, "False", username))

        # Commit the changes and close the connection
        connection.commit()

        # Close the connection
        connection.close()

    except sqlite3.Error as error:
        print(f"Error retrieving OTP: {error}")
        return None


@app.route('/check-otp', methods=['POST'])
def check_otp():
    print("Function is called!")
    if request.method == 'POST':
        otp = request.form.get('input-otp')

        # Get the username argument from the URL
        username = request.form.get('username')
        print("USERNAME: ", username)

        try:
            if otp == retrieve_otp():
                enter_other_entered_otps(username, retrieve_otp(), otp, match=True)
            else:
                enter_other_entered_otps(username, retrieve_otp(), otp, match=False)
            return jsonify({'status': 'success', 'message': 'OTP verified'})
        except TypeError:
            print(otp, retrieve_otp())
            if otp == retrieve_otp():
                if_iteration_is_none(username, retrieve_otp(), otp)
                return jsonify({'status': 'success', 'message': 'OTP verified but error in iteration'})
            else:
                return jsonify({'status': 'error', 'message': 'Invalid OTP'})


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8100)
