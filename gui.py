# Libs
import flet as ft
from config import BANNER_PATH, APP_NAME, command_s, command_d, load_password
from func import run_command, open_anydesk, open_settings_dialog

# UI.
def create_ui(page: ft.Page):
    page.title = APP_NAME
    page.bgcolor = ft.colors.WHITE
    page.window_width = 400
    page.window_height = 500
    page.window_resizable = False
    page.theme_mode = ft.ThemeMode.LIGHT
    page.update()

    # Load and display the banner image at the top of the UI:
    banner = ft.Image(src=BANNER_PATH, width=380, height=150)

    # Button to set a password, with success and error messages:
    set_pw_button = ft.ElevatedButton(
        "Establecer Contraseña", 
        on_click=lambda _: run_command(command_s(load_password()), "Contraseña establecida correctamente", "Error al establecer la contraseña", page), 
        width=200, 
        color="#ffffff", 
        bgcolor="red"
    )

    # Button to delete the password, with success and error messages:
    delete_pw_button = ft.ElevatedButton(
        "Eliminar Contraseña", 
        on_click=lambda _: run_command(command_d, "Contraseña eliminada correctamente", "Error al eliminar la contraseña", page), 
        width=200, 
        color="#ffffff", 
        bgcolor="red"
    )

    # Button to start AnyDesk application with icon:
    anydesk_button = ft.ElevatedButton(
        "Iniciar AnyDesk",
        on_click=lambda _: open_anydesk(),
        icon=ft.icons.DESKTOP_WINDOWS,
        width=200,
        color="#ffffff",
        bgcolor="red"
    )

    # Button to open settings dialog in the application:
    settings_button = ft.ElevatedButton(
        "Configuración", 
        on_click=lambda _: open_settings_dialog(page), 
        width=200, 
        color="#ffffff", 
        bgcolor="red"
    )

    # Footer text displaying developer information and license details:
    footer_label = ft.Text(
        "Desarrollado por Denis Gontero - 2024 Licencia Libre.",
        size=12,
        color="red",
        text_align="center",
        weight=ft.FontWeight.BOLD  
    )

    # Add all components to the main UI layout:
    page.add(
        ft.Column(
            [
                banner,
                ft.Column(
                    [set_pw_button, delete_pw_button, anydesk_button, settings_button],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20
                ),
                ft.Container(height=50),
                footer_label
            ],

            # Arrange components in a column with spacing and alignment:
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            expand=True
        )
    )
