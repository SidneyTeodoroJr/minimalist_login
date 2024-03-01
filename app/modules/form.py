import flet as ft

submit = ft.ElevatedButton(
                "SUBMIT", 
                color=ft.colors.BLUE, 
                bgcolor=ft.colors.GREY_900, 
                icon=ft.icons.LOGIN_SHARP,
        )

user = ft.Icon(
            name=ft.icons.PERSON_PIN_SHARP, 
            color=ft.colors.WHITE, 
            size=60
        )

email= ft.TextField(
            label="Email", 
            border_radius=ft.border_radius.all(30), 
            icon=ft.icons.EMAIL
        )

password= ft.TextField(
            label="Password", 
            border_radius=ft.border_radius.all(30), 
            password=True, 
            icon=ft.icons.LOCK
        )