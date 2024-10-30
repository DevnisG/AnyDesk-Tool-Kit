" ANYDESK TOOL KIT "

# Libs
import os
import sys
import ctypes
import flet as ft
from config import setup_db
from gui import create_ui

# Function to restart the script with admin privileges if required:
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Uses Windows ShellExecute to re-run the script as administrator:
def run_as_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{os.path.abspath(__file__)}"', None, 1)

# Function to initialize and run the main GUI of the application:
def main(page: ft.Page):
    create_ui(page)

# Main application logic
if __name__ == "__main__":
    setup_db()
    if not is_admin():
        run_as_admin()
        sys.exit()
    ft.app(target=main)