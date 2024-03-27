import sqlite3


def create_database():
    import sqlite3
    import datetime

    conn = sqlite3.connect(
        r'B:\Computer Science and Engineering\PycharmIDE\ManipalAttendanceProjectV2\Database\database.db')
    cur = conn.cursor()

    date = datetime.datetime.now().strftime("%Y_%m_%d")
    print(date)

    # Corrected SQL statement
    cur.execute(
        f"""CREATE TABLE IF NOT EXISTS map_class_to_coordinates(class TEXT, X1 TEXT, Y1 TEXT, X2 TEXT, Y2 TEXT, X3 TEXT, Y3 TEXT, X4 TEXT, Y4 TEXT)""")
    conn.commit()
    conn.close()



def delete_table():
    conn = sqlite3.connect(
        r'B:\Computer Science and Engineering\PycharmIDE\ManipalAttendanceProjectV1\Database\database.db')
    cur = conn.cursor()
    cur.execute("DROP TABLE check_otps_entered")
    conn.commit()
    conn.close()


def insert():
    conn = sqlite3.connect(
        r'B:\Computer Science and Engineering\PycharmIDE\ManipalAttendanceProjectV2\Database\database.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO map_class_to_coordinates VALUES('206', '26.842807', '75.565815', '26.842922', '75.566111', '26.84336', '75.565585', '26.843453', '75.565878')")
    conn.commit()
    conn.close()

insert()


def update_attendance_otps_to_null():
    conn = sqlite3.connect(
        r'B:\Computer Science and Engineering\PycharmIDE\ManipalAttendanceProjectV2\Database\database.db')
    cur = conn.cursor()
    cur.execute(
        "UPDATE check_otps_entered SET iteration = NULL, fo1 = NULL, fu1 = NULL, fo2 = NULL, fu2 = NULL, fo3 = NULL, fu3 = NULL, fo4 = NULL, fu4 = NULL, fo5 = NULL, fu5 = NULL")
    conn.commit()
    conn.close()


