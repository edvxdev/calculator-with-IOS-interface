import flet as ft  
from flet import colors
from decimal import Decimal

botoes = [
    {'operador': 'AC', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '±', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '%', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '/', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '7', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '8', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '9', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '*', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '4', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '5', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '6', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '-', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '1', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '2', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '3', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '+', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '0', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '.', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '=', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
]

def main(page: ft.Page):
    page.bgcolor = '#000'
    page.window_resizable = False
    page.window_width = 280
    page.window_height = 400
    page.title = 'Calculadora'
    page.window_always_on_top = True
    
    result = ft.Text(value='0', color = colors.WHITE, size=25)
    
    def calculate(operator, value_at):
        try:
            value = eval(value_at)

            if operator == '%':
                value /= 100
            elif operator == '±':
                value = -value
        except:
            return 'Error'
        
        digits = min(abs(Decimal(value).as_tuple().exponent), 5)
        return format(value, f'.{digits}f')
    
    def select(e):
        value_at = result.value if result.value not in ('0', 'Error') else ''
        value = e.control.content.value
        
        if value.isdigit():
            value = value_at + value
        elif value == 'AC':
            value = '0'
        else:
            if value_at and value_at[-1] in ('/', '*', '+', '-', '.'):
                value_at = value_at[:-1]
            
            value = value_at + value
            
            if value[-1] in ('=', '%', '±'):
                value = value = calculate(operator=value[-1], value_at=value_at)
         
        result.value = value 
        result.update()       
    
    btn = [ft.Container(
        content = ft.Text(value=btn['operador'], color=btn['fonte']),
        alignment = ft.alignment.center, 
        width = 50,
        height = 50,  
        bgcolor = btn['fundo'],        
        border_radius = 100,
        on_click = select
      ) for btn in botoes]
    
    display = ft.Row(
        width = 250, 
        controls = [result],
        alignment = 'end'
    )
    
    keyboard = ft.Row(
        width = 250,
        wrap = True,
        controls = btn,
        alignment = 'end'
)

    page.add(display,keyboard)
    
ft.app(target = main)