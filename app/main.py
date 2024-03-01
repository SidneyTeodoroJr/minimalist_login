# Importing dependencies
import flet as ft  
# Importing the modules
from modules.custom_text import *
from modules.form import *  

def main(page: ft.page):
    page.title = "Minimalist Login"  
    page.theme_mode = ft.ThemeMode.DARK  
    page.scroll = "auto"  

    page.window_maximizable = False  
    page.window_minimizable = False  

    page.vertical_alignment = ft.MainAxisAlignment.CENTER  
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  

    page.add( 
        # Empty container for spacing
        ft.Container( 
            height=100
        ),
        # Login form container
        ft.Container(  
            alignment=ft.alignment.center,
            bgcolor=ft.colors.GREY_900,
            width=500,
            height=500,
            border_radius=ft.border_radius.all(10),
            shadow=ft.BoxShadow(blur_radius=50, color=ft.colors.BLUE_900),
            # Form content organized into columns
            content=ft.Column([  
                ft.Row([  
                    user
                ], alignment="center", offset=ft.transform.Offset(0, 0.3)),
                ft.Row([  
                    title(value="USER LOGIN"),
                ], alignment="center", offset=ft.transform.Offset(0, 0.3)),
                ft.Row([  
                    subtitle(value="Log in with your account to have access"),
                ], alignment="center"),
                ft.Row([  
                    email
                ], alignment="center", offset=ft.transform.Offset(0, 0.3)),
                ft.Row([  
                    password
                ], alignment="center", offset=ft.transform.Offset(0, 0.3)),
                ft.Row([  
                    submit
                ], alignment="center", offset=ft.transform.Offset(0, 1)),
                ft.Row([  
                    link(value="Recuperar senha")
                ], alignment="left", offset=ft.transform.Offset(0.1, 7))
            ])
        ),
        ft.Container(  
            height=100
        ),
    )

    page.update()  # Update the page with changes
ft.app(target=main)  # Run the application with the main function as target