import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """Membuat koneksi ke database."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Connected to MySQL database")
        except Error as e:
            print(f"Error: {e}")

    def close(self):
        """Menutup koneksi ke database."""
        if self.connection.is_connected():
            self.connection.close()
            print("Connection to MySQL database closed")

    def register_user(self, username, password):
        """Mendaftarkan pengguna baru di database."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            return False  # Username already exists
        
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        self.connection.commit()
        cursor.close()
        return True

    def validate_user(self, username, password):
        """Memvalidasi kredensial pengguna."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        
        return user is not None