from Modulos import Modulo_Muebles as Muebles

from Modulos.Modulo_Util import (
    CleanScreen
)

from Modulos.Modulo_ShowPrint import (
    Title,
    Continue,
    Separator
)

from Modulos.Modulo_Language import (
    get_text as Lang,
    YesNo
)


def Menu_Muebles():
    loop = True
    while loop == True:
        CleanScreen()
        # Menu - Parte Visual
        Title( Lang('gen_furniture') )
        print(
            f'1. {Lang("corner_shelving")}\n'
            f'2. {Lang("table")}\n'
            f'0. {Lang("exit")}'
        )
        option = input(f"{Lang('set_option')}: ")
        
        # Continuer con la opcion elegida
        continue_or_not = Continue()
        if continue_or_not == YesNo('yes'):
            pass
        else:
            option = None
    
        # Menu - Opcion elegida
        furniture = False
        if option == '1':
            furniture = Corner_shelving()

        elif option == '2':
            furniture = Table()
            
        elif option == '0':
            loop = False
        
        elif option == None:
            pass
            
        else:
            Continue(
                option,
                message_error=True
            )
        
        # Imprimir datos para armar el mueble
        if type(furniture) is str:
            input(
                furniture + '\n\n'
                f"{Lang('continue_enter')}..."
            )
        elif furniture == None:
            input(
                'ERROR\n'
                f"{Lang('continue_enter')}..."
            )
        else:
            pass


def Corner_shelving():
    # Esquinero - Parte visual
    CleanScreen()
    Title( Lang('corner_shelving') )

    try:
        thickness = float( input(f'{Lang("thickness")}: ') )
        width = float( input(f'{Lang("width")}: ') )
        height = float( input(f'{Lang("height")}: ') )
    except:
        thickness = None
        width = None
        height = None
    
    # Esquinero - Opcion elegida
    CleanScreen()
    if (
        type(thickness) is float or
        type(width) is float or
        type(height) is float
    ):
        return Muebles.Corner_shelving(
            thickness=thickness,
            width=width,
            height=height,
            round_number=False
        )
    else:
        return None


def Table():
    # Mesa - Parte visual
    CleanScreen()
    Title( Lang('table') )

    try:
        thickness = float( input(f'{Lang("thickness")}: ') )
        width = float( input(f'{Lang("width")}: ') )
        height = float( input(f'{Lang("height")}: ') )
    except:
        thickness = None
        width = None
        height = None
    
    # Mesa - Opcion elegida
    CleanScreen()
    if (
        type(thickness) is float or
        type(width) is float or
        type(height) is float
    ):
        return Muebles.Table(
            thickness=thickness,
            width=width,
            height=height,
            round_number=False
        )
    else:
        return None


if __name__ == '__main__':
    Menu_Muebles()