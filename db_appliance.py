import sqlite3
from binaryTransformation import convertToBinaryData


def createTable(current_date):
    if not isinstance(current_date, str):
        raise TypeError
    try:
        sqliteConnection = sqlite3.connect("car_plates.db")
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqltite_create_table = """CREATE TABLE IF NOT EXISTS {table_name}(datestamp TEXT, vehicle BLOP, registration_number TEXT)""".format(
            table_name=current_date
        )

        cursor.execute(sqltite_create_table)
        sqliteConnection.commit()
        print("Table successfully created")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to create table:", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The sqlite connection is closed\n")


def insertResult(current_date, datestamp, vehicle_photo, reg_num):
    if not all(
        isinstance(i, str) for i in [current_date, datestamp, vehicle_photo, reg_num]
    ):
        raise TypeError
    try:
        sqliteConnection = sqlite3.connect("car_plates.db")
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        ext = [".jpg", ".png"]
        if vehicle_photo.endswith(tuple(ext)) and isinstance(
            convertToBinaryData(vehicle_photo), bytes
        ):
            pass
        else:
            print("Unsuitable image path")
            raise TypeError

        binaryVehiclePh = convertToBinaryData(vehicle_photo)
        sqlite_insert_blob_query = """INSERT INTO {table_name} (datestamp, vehicle, registration_number) VALUES (?, ?, ?)""".format(
            table_name=current_date
        )
        data_tuple = (datestamp, binaryVehiclePh, reg_num)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table -", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")
