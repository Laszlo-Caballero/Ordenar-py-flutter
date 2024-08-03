import flet as ft


async def main(page: ft.Page):
    page.title = "first app flet"
    page.window.width = 720
    page.window.height = 720

    superior = ft.Container(width=600, height=200, margin=ft.margin.only(top=20), border=ft.border.all())
    centro = ft.Container(width=600, height=500, margin=ft.margin.only(top=20), border=ft.border.all())
    inferior = ft.Container(width=600, height=200, margin=ft.margin.only(top=20), border=ft.border.all())

    col = ft.Column(spacing=0 , controls=[
        superior,
        centro,
        inferior
    ])


    contenedor = ft.Container(col, width=720, height=1280, alignment=ft.alignment.top_center)

    await page.add(contenedor)

ft.app(main)