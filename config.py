# Libs
import os
import sqlite3

# Define paths for application components, including app name, banner image, AnyDesk executable, and database:
APP_NAME = "AnyDesk Tool Kit"
BANNER_PATH = "banner.png"
ANYDESK_PATH = r"C:\Program Files (x86)\AnyDesk\AnyDesk.exe"
DB_PATH = "settings.db"

# Define commands to interact with AnyDesk API for setting and removing the password:
command_s = lambda pw: f'echo {pw} | "{ANYDESK_PATH}" --set-password'
command_d = f'"{ANYDESK_PATH}" --remove-password'

# Function to initialize the database:
def setup_db():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS settings (id INTEGER PRIMARY KEY, password TEXT)''')

# Function to save the password into the database:
def save_password(password):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('DELETE FROM settings')
        c.execute('INSERT INTO settings (password) VALUES (?)', (password,))

# Function to load the stored password from the database:
def load_password():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('SELECT password FROM settings')
        result = c.fetchone()
    return result[0] if result else ""