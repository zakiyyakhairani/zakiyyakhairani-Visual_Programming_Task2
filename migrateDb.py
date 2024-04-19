import mysql.connector

def migrate_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pemesanan kopi"
        )
        if connection.is_connected():
            cursor = connection.cursor()
            # Definisikan perintah SQL untuk membuat tabel baru
            create_table_query = """
                CREATE TABLE IF NOT EXISTS kopi(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nama_lengkap VARCHAR(255),
                    nim VARCHAR(20),
                    url_github VARCHAR(255),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                )
            """
            # Eksekusi perintah SQL
            cursor.execute(create_table_query)
            print("Tabel berhasil dibuat.")
            cursor.close()
    except mysql.connector.Error as err:
        print("Error: ", err)
    finally:
        if connection.is_connected():
            connection.close()

if _name_ == "_main_":
    migrate_database()