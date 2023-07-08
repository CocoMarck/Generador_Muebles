from .Modulo_Language import get_text as Lang


def Corner_shelving(
    thickness = 0.1,
    width = 1.0,
    height = 4.0,
    round_number = False
):
    '''
    Un Esquinero. Un mueble vertical para guardar y ordenar objetos.
    
    Parametros:
    thickness, # float or int
    width, # float or int
    height, # float or int

    round_number, # bool
    # El parametro round_number sirve para redondear los numeros recividos y retornados.
    '''
    # Mitad de grosor
    half_thickness = thickness / 2
    
    # Parte - Repisas/Cuadrado
    square = width - half_thickness
    count_shelf = int ( height/width + 1 )
    # text_shelf = f'{square}cm X {square}cm'
    
    # Parte - Pared/Rectangulo
    rectangle = height + half_thickness
    # text_wall_type1 = f'{square}cm X {rectangle}cm'
    # text_wall_type2 = f'{width}cm X {rectangle}cm'
    
    # Parte - Soporte/Opcional
    # text_support = f'{thickness*2}cm X {rectangle}cm'
    
    # Redondear o no, los parametros y las partes del esquinero
    if round_number == True:
        # Parametros
        thickness = round(thickness)
        width = round(width)
        height = round(height)
        # Redondear numeros de partes
        square = round(square)
        rectangle = round(rectangle)
    else:
        # No redondear, pero si solo mostrar cuatro decimales
        square = round(square, 4)
        rectangle = round(rectangle, 4)
    
    # Esquinero - Texto terminado, y texto final
    text_shelf = f'{square}cm X {square}cm'
    text_wall_type1 = f'{square}cm X {rectangle}cm'
    text_wall_type2 = f'{width}cm X {rectangle}cm'
    text_support = f'{thickness*2}cm X {rectangle}cm'
    
    text_corner_shelving = (
        f'{Lang("measures_corner_shelving")}\n'
        f'    {Lang("thickness")}: {thickness}\n'
        f'    {Lang("width")}: {width}\n'
        f'    {Lang("height")}: {height}\n'
        '\n'
        '\n'
        f'{count_shelf} {Lang("shelf_square")}\n'
        f'    {text_shelf}\n'
        '\n'
        f'2 {Lang("rectangular_wall")}\n'
        f'    1 de {text_wall_type1}\n'
        f'    1 de {text_wall_type2}\n'
        '\n'
        f'1 {Lang("part_support")} ({Lang("optional")})\n'
        f'    {text_support}'
    )
    
    return text_corner_shelving


def Table(
    thickness = 0.1,
    width = 2.0,
    height = 2.0,
    round_number = False
):
    '''
    Un Mesa para multi usos.
    Recive unos datos de medida (numero type float), grosor, ancho y alto y te devuelve un texto, que te indica las partes necesarias para hacer una mesa.
    
    Parametros
    thickness, # float or int
    width, # float or int
    height, # float or int

    round_number, # bool
    # El parametro round_number sirve para redondear los numeros recividos y retornados.
    '''

    # Mesa - Parte principal
    part_main = width / 2
    # text_main = f'{width}cm X {part_main}cm'
    
    # Mesa - Soporte tipo 1
    part_support = thickness*2 + thickness / 2
    # text_support_type1 = f'{part_support}cm X {part_main}cm'
    
    # Mesa - Soporte tipo 2
    part_support0 = thickness*3
    part_support1 = width - part_support0*2
    # text_support_type2 = f'{part_support0}cm X {part_support1}'
    
    # Mesa Patas
    # text_leg = f'{part_support0}cm X {height}cm'
    
    # Redondear o no, los paramteros y las partes de la mesa
    if round_number == True:
        # Parametros
        thickness = round(thickness)
        width = round(width)
        height = round(height)
        # Redondear numeros de partes
        part_main = round(part_main)
        part_support = round(part_support)
        part_support0 = round(part_support0)
        part_support1 = round(part_support1)
    else:
        # No redondear, pero si solo mostrar cuatro decimales
        part_main = round(part_main, 4)
        part_support = round(part_support, 4)
        part_support0 = round(part_support0, 4)
        part_support1 = round(part_support1, 4)
    
    # Mesa - Texto Terminado
    text_main = f'{width}cm X {part_main}cm'
    text_support_type1 = f'{part_support}cm X {part_main}cm'
    text_support_type2 = f'{part_support0}cm X {part_support1}'
    text_leg = f'{part_support0}cm X {height}cm'
    
    text_table = (
        f'{Lang("measures_corner_shelving")}\n'
        f'    Grosor: {thickness}\n'
        f'    Achura: {width}\n'
        f'    Altura: {height}\n'
        '\n'
        '\n'
        f'1 {Lang("part_main")}\n'
        f'    {text_main}\n'
        '\n'
        f'4 {Lang("part_support")}\n'
        f'    2 de {text_support_type1}\n'
        f'    2 de {text_support_type2}\n'
        '\n'
        f'4 {Lang("paw")}\n'
        f'    {text_leg}'
    )
    
    return text_table