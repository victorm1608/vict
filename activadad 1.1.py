import flet as ft


def main(page: ft.Page):
    page.title = "calculadora de IMC"
    page.bgcolor"purple"
    
    txtpaso=ft.TextField(label="ingresar el peso")
    txtAltura=ft.TextField(label="ingresa la altura")
    lbLIMC=ft.text("tu imagen es: ")
    img=ft.imagen(src=""https://github.com/Prof-Luis1986/Recursos/blob/main/Bascula.png,
                width=200
                heigth=200
    
    )

btncalcular=ft.ElevatedButton(text="calcular")
btnlimpiar=ft.ElevatedButton(text="limpiar")

page.add(
    ft.column(
        controls[txtPeso,
                txtAltura,
                lblIMC
                ],alignment="CENTER"
        ft.Row(
            controls=[
                btncalcular,
                btnlimpiar
            ],alignment="CENTER"
        )
    )
    
)













ft.app(target=main,view=ft.AppView.WEB_BROWSER)
