from data.Modulo_Language import get_text as Lang


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
        pass
        # No redondear, pero si solo mostrar cuatro decimales
        # square = round(square, 4)
        # rectangle = round(rectangle, 4)
        
    # Base sugerida para sacar las piezas
    list_width = [
        square, square, width, thickness*2
        # Repisas, Pared tipo1, Pared tipo2, Soporte opcional
    ]
    base_width = 0.0
    for number in list_width:
        base_width += float(number)
    
    list_height = [
        square*count_shelf, rectangle, rectangle, rectangle
        # Repisas, Pared tipo1, Pared tipo2, Soporte opcional
    ]
    base_height = 0.0
    for number in list_height:
        base_height += float(number)

    if base_width < base_height:
        # Obtener el numero mas alto de una lista de numeros
        list_height = [
            square*count_shelf, rectangle, rectangle, rectangle
            # Sin contar si hay mas de uno
            # Repisas, Pared tipo1, Pared tipo2, Soporte opcional
        ]
        base_height = None
        for number in list_height:
            if (base_height is None or number > base_height):
                base_height = number
    else:
        # Obtener el numero mas alto de una lista de numeros
        list_width = [
            square, square, width, thickness*2
            # Sin contar si hay mas de uno
            # Repisas, Pared tipo1, Pared tipo2, Soporte opcional
        ]
        base_width = None
        for number in list_width:
            if (base_width is None or number > base_width):
                base_width = number

    # Para que la base pueda tener un rango de error:
    base_width = round(base_width * 1.1)
    base_height = round(base_height * 1.1)
    
    # Esquinero - Texto terminado, y texto final
    text_shelf = f'{square}cm X {square}cm'
    text_wall_type1 = f'{square}cm X {rectangle}cm'
    text_wall_type2 = f'{width}cm X {rectangle}cm'
    text_support = f'{thickness*2}cm X {rectangle}cm'
    text_base = f'{base_width}cm X {base_height}cm'
    
    text_corner_shelving = (
        f'{Lang("measures_corner_shelving")}\n'
        f'    {Lang("thickness")}: {thickness}\n'
        f'    {Lang("width")} X {Lang("height")}: '
        f'{width} X {height}\n'
        '\n'
        f'{Lang("suggest_base_for_parts")}:\n'
        f'    {Lang("thickness")}: {thickness}\n'
        f'    {Lang("size")}: {text_base}\n'
        '\n'
        '\n'
        f'{Lang("parts")}:\n'
        f'{count_shelf} {Lang("shelf_square")}\n'
        f'    {text_shelf}\n'
        '\n'
        f'2 {Lang("rectangular_wall")}\n'
        f'    1 {Lang("of")}: {text_wall_type1}\n'
        f'    1 {Lang("of")}: {text_wall_type2}\n'
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
        pass
        # No redondear, pero si solo mostrar cuatro decimales
        # part_main = round(part_main, 4)
        # part_support = round(part_support, 4)
        # part_support0 = round(part_support0, 4)
        # part_support1 = round(part_support1, 4)
    
    # Base sugerida para obtener las piezas
    list_width = [
        width, part_support*2, part_support0*2, part_support0*4
        # Principal, soporte tipo 1, sporte tipo 2, patas
    ]
    base_width = 0.0
    for number in list_width:
        base_width += float(number)
    
    list_height = [
        part_main, part_main*2, part_support1*2, height*4
        # Principal, soporte tipo 1, sporte tipo 2, patas
    ]
    base_height = 0.0
    for number in list_height:
        base_height += float(number)

    if base_width < base_height:
        # Obtener el numero mas alto de una lista de numeros
        list_height = [
            part_main, part_main, part_support1, height
            # Sin contar si hay mas de uno.
            # Principal, soporte tipo 1, sporte tipo 2, patas
        ]
        base_height = None
        for number in list_height:
            if (base_height is None or number > base_height):
                base_height = number
    else:
        # Obtener el numero mas alto de una lista de numeros
        base_width = None
        list_width = [
            width, part_support, part_support0, part_support0
            # Sin contar si hay mas de uno
            # Principal, soporte tipo 1, sporte tipo 2, patas
        ]
        for number in list_width:
            if (base_width is None or number > base_width):
                base_width = number

    # Para que la base pueda tener un rango de error:
    base_width = round(base_width * 1.1)
    base_height = round(base_height * 1.1)
    
    # Mesa - Texto Terminado
    text_main = f'{width}cm X {part_main}cm'
    text_support_type1 = f'{part_support}cm X {part_main}cm'
    text_support_type2 = f'{part_support0}cm X {part_support1}cm'
    text_leg = f'{part_support0}cm X {height}cm'
    text_base = f'{base_width}cm X {base_height}cm'
    
    text_table = (
        f'{Lang("measures_table")}\n'
        f'    {Lang("thickness")}: {thickness}\n'
        f'    {Lang("width")} X {Lang("height")}: '
        f'{width} X {height}\n'
        '\n'
        f'{Lang("suggest_base_for_parts")}:\n'
        f'    {Lang("thickness")}: {thickness}\n'
        f'    {Lang("size")}: {text_base}\n'
        '\n'
        '\n'
        f'{Lang("parts")}:\n'
        f'1 {Lang("part_main")}\n'
        f'    {text_main}\n'
        '\n'
        f'4 {Lang("part_support")}\n'
        f'    2 {Lang("of")}: {text_support_type1}\n'
        f'    2 {Lang("of")}: {text_support_type2}\n'
        '\n'
        f'4 {Lang("paw")}\n'
        f'    {text_leg}'
    )
    
    return text_table





def Ramp(width=10, height=4, thickness=2, round_number = False):
    '''
    Para armar una rampa
    '''
    size_input = (width, height)
    # Si la altura y anchura son las mismas
    height -= thickness

    if height == width:
        third_side = width
    else:    
        third_side = ( (height*height) + (width*width) )**(0.5)

    third_side_half = (third_side/2)+(thickness*2)
    
    
    # Partes
    # rect-down y rect-lateral son partes opcionales.
    dict_parts = {
        'triangle' : [2, width, height, third_side],
        'rect-up' : [1, third_side, third_side_half],
        'rect-down' : [1, (width+thickness), third_side_half],
        'rect-lateral' : [1, third_side_half, (height+thickness)]
    }
    
    
    
    # Devolver lo necesario
    text = ''

    for key in dict_parts.keys():
        part = dict_parts[key]
        
        part_last_index = len(part) -1
        part_count = 0
        for x in part:
            if part_count > 0:
                if part_count == part_last_index:
                    text += f'{part[part_count]}'
                else:
                    text += f'{part[part_count]} X '
            else:
                text += (
                    f'{part[part_count]} {key}:\n'
                    '    '
                )
            part_count += 1
        
        text += '\n\n'

    return text