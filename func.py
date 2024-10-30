# Libs
import flet as ft
import subprocess
from config import ANYDESK_PATH, command_s, command_d, save_password, load_password

# Function to execute a shell command to set or delete a password:
def run_command(command, success_message, error_message, page):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"Output_result: {result.stdout}")
        alert_box("OK", success_message, page)
    except subprocess.CalledProcessError as e:
        print(f"ERROR: {e.stderr}")
        alert_box("Error", error_message, page)

# Function to open the AnyDesk application using its executable path:
def open_anydesk():
    subprocess.Popen(ANYDESK_PATH)

# Function to display alert dialogs with a title and message:
def alert_box(title, message, page):
    def close_dialog(e):
        dialog.open = False
        page.update()

# Includes a close button to dismiss the alert dialog:
    dialog = ft.AlertDialog(
        title=ft.Row([
            ft.Text(title),
            ft.IconButton(ft.icons.CLOSE, on_click=close_dialog)
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        content=ft.Text(message),
        actions=[], 
        actions_alignment=ft.MainAxisAlignment.END,
    )

    page.dialog = dialog
    dialog.open = True
    page.update()

# Function to open the settings dialog where users can update the password:
def open_settings_dialog(page):
    def save_settings(e):
        password = password_field.value
        save_password(password)
        alert_box("Configuración", "Contraseña guardada exitosamente.", page)
        dialog.open = False
        page.update()

    def close_dialog(e):
        dialog.open = False
        page.update()

# Row layout for password field and visibility icon, centered alignment:
    def toggle_password_visibility(e):
        password_field.password = not password_field.password
        eye_icon.icon = ft.icons.VISIBILITY_OFF if password_field.password else ft.icons.VISIBILITY
        page.update()

    password_field = ft.TextField(
        value=load_password(),
        label="Nueva Contraseña",
        width=200,
        password=True,
        color="black"
    )

    eye_icon = ft.IconButton(
        ft.icons.VISIBILITY_OFF,
        on_click=toggle_password_visibility
    )

    password_row = ft.Row(
        [password_field, eye_icon],
        alignment=ft.MainAxisAlignment.CENTER
    )

    save_button = ft.ElevatedButton("Guardar Configuración", on_click=save_settings, width=200, color="white", bgcolor="red")

    dialog = ft.AlertDialog(
        title=ft.Row([
            ft.Text("Configuración", size=24, color="red"),
            ft.IconButton(ft.icons.CLOSE, on_click=close_dialog)
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        content=ft.Column([password_row, save_button], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
        actions=[],
        actions_alignment=ft.MainAxisAlignment.END,
    )

# Opens the dialog when settings are accessed, with password field and save button
    page.dialog = dialog
    dialog.open = True
    page.update()