import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib, GdkPixbuf

from Interface import Modulo_Util_Gtk as Util_Gtk
from Modulos import Modulo_Muebles as Muebles
from Modulos.Modulo_Language import get_text as Lang


class Window_Main(Gtk.Window):
    def __init__(self):
        super().__init__( title=Lang('gen_furniture') )
        self.set_resizable(True)
        self.set_default_size(308, -1)
        
        # Contenedor Principal
        vbox_main = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, spacing=8
        )
        
        # Seccion Vertical - Esquinero
        button_corner_shelving = Gtk.Button(
            label=Lang('corner_shelving') 
        )
        button_corner_shelving.connect(
            'clicked', self.evt_corner_shelving
        )
        vbox_main.pack_start(button_corner_shelving, False, True, 0)
        
        # Seccion Vertical - Mesa
        button_table = Gtk.Button(
            label=Lang('table')
        )
        button_table.connect('clicked', self.evt_table)
        vbox_main.pack_start(button_table, False, True, 0)
        
        # Seccion Vertical final - Salir
        button_exit = Gtk.Button(
            label=Lang('exit')
        )
        button_exit.connect('clicked', self.evt_exit)
        vbox_main.pack_end(button_exit, False, True, 16)
        
        # Fin, Mostrar ventana y todo el contenido
        self.add(vbox_main)
        self.show_all()
    
    def evt_corner_shelving(self, widget):
        self.hide()
        dialog = Dialog_Furniture(self, furniture='corner_shelving')
        dialog.run()
        dialog.destroy()
        self.show_all()
    
    def evt_table(self, widget):
        self.hide()
        dialog = Dialog_Furniture(self, furniture='table')
        dialog.run()
        dialog.destroy()
        self.show_all()
    
    def evt_exit(self, widget):
        self.destroy()


class Dialog_Furniture(Gtk.Dialog):
    def __init__(self, parent, furniture='corner_shelving'):
        super().__init__(
            title=Lang(furniture),
            transient_for=parent, flags=0,
        )
        self.furniture = furniture
        #self.set_title(Lang(furniture))
        self.set_default_size(308, 128)
        
        # Contenedor Pincipal
        vbox_main = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, spacing=8
        )
        vbox_main.set_property('expand', True)
        
        # Seccion Vertical - Grosor
        hbox = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL, spacing=8
        )
        vbox_main.pack_start(hbox, False, True, 0)
        
        label_thickness = Gtk.Label( label=Lang('thickness') )
        hbox.pack_start(label_thickness, False, True, 0)
        
        self.entry_thickness = Gtk.Entry()
        self.entry_thickness.set_placeholder_text( Lang('cm') )
        self.entry_thickness.connect(
            'changed', self.on_entry_onlyNumber
        )
        hbox.pack_end(self.entry_thickness, False, True, 0)
        
        # Seccion Vertical - Ancho
        hbox = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL, spacing=8
        )
        vbox_main.pack_start(hbox, False, True, 0)
        
        label_width = Gtk.Label( label=Lang('width') )
        hbox.pack_start(label_width, False, True, 0)
        
        self.entry_width = Gtk.Entry()
        self.entry_width.set_placeholder_text( Lang('cm') )
        self.entry_width.connect(
            'changed', self.on_entry_onlyNumber
        )
        hbox.pack_end(self.entry_width, False, True, 0)
        
        # Seccion Vertical - Alto
        hbox = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL, spacing=8
        )
        vbox_main.pack_start(hbox, False, True, 0)
        
        label_height = Gtk.Label( label=Lang('height') )
        hbox.pack_start(label_height, False, True, 0)
        
        self.entry_height = Gtk.Entry()
        self.entry_height.set_placeholder_text( Lang('cm') )
        self.entry_height.connect(
            'changed', self.on_entry_onlyNumber
        )
        hbox.pack_end(self.entry_height, False, True, 0)
        
        # Seccion Vertical Final - Obtener mueble
        button_get_furniture = Gtk.Button(
            label=Lang('get_furniture')
        )
        button_get_furniture.connect(
            'clicked', self.evt_get_furniture
        )
        vbox_main.pack_end(button_get_furniture, False, True, 16)
        
        # Fin, Mostrar ventana y todo
        self.get_content_area().add(vbox_main)
        self.show_all()
    
    def on_entry_onlyNumber(self, entry):
        # Aceptar solo caracteres de tipo numero
        text = entry.get_text().strip()
        entry.set_text(
            ''.join(
                [ i for i in text if i in '0123456789.']
            )
        )
    
    def evt_get_furniture(self, widget):
        # Verificar si es cero o no
        if (
            self.entry_thickness.get_text() == '0' or
            self.entry_width.get_text() == '0' or
            self.entry_height.get_text() == '0'
        ):
            # Si es cero, entonces los caracteres seran nulos o ''
            self.entry_thickness.set_text('')
            self.entry_width.set_text('')
            self.entry_height.set_text('')
        else:
            pass

        # Si es posible, obtener datos del mueble
        try:
            # Obtencion de datos para armar mueble
            thickness = float(self.entry_thickness.get_text())
            width = float(self.entry_width.get_text())
            height = float(self.entry_height.get_text())
            
            # Eleccion del mueble, dependiendo del parametro furniture
            if self.furniture == 'corner_shelving':
                text_furniture = Muebles.Corner_shelving(
                    thickness=thickness,
                    width=width,
                    height=height
                )
            elif self.furniture == 'table':
                text_furniture = Muebles.Table(
                    thickness=thickness,
                    width=width,
                    height=height
                )
                
        except:
            # Datos erroneos
            text_furniture = 'ERROR'
        
        self.hide()
        dialog = Dialog_View_TextImage(
            self,
            text=text_furniture,
            image_from_file=f'./Images/furniture_{self.furniture}.png'
        )
        dialog.run()
        dialog.destroy()
        self.destroy()


class Dialog_View_TextImage(Gtk.Dialog):
    def __init__(
        self, parent,
        text=None, image_from_file=None
    ):
        super().__init__(
            title=Lang('text&image'),
            transient_for=parent, flags=0
        )
        self.set_default_size(512, 512)
        
        # Contenedor principal
        hbox_main = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL, spacing=8
        )
        hbox_main.set_property('expand', True)
        
        # Seccion Horizontal de Text View
        if text == None:
            pass
        else:
            # Scroll
            scroll_text = Gtk.ScrolledWindow()
            scroll_text.set_hexpand(True)
            scroll_text.set_vexpand(True)
            hbox_main.pack_start(scroll_text, True, True, 0)
            
            # Text View - Texto
            text_view = Gtk.TextView()
            text_view.set_editable(False)
            buffer_text = text_view.get_buffer()
            buffer_text.set_text(text)
            scroll_text.add(text_view)
        
        # Seccion Horizontal de Imagen
        if image_from_file == None:
            pass
        else:
            # Scroll
            scroll_image = Gtk.ScrolledWindow()
            scroll_image.set_hexpand(True)
            scroll_image.set_vexpand(True)
            hbox_main.pack_start(scroll_image, True, True, 0)
            
            # Text View - Texto
            image = Gtk.Image()
            pixbuf_image = GdkPixbuf.Pixbuf.new_from_file_at_size(
                image_from_file, # Ruta de Imagen
                256, 256 # Ancho X Alto
            )
            image.set_from_pixbuf(pixbuf_image)
            scroll_image.add(image)
        
        # Fin, agregar contenido y mostrar todo
        self.get_content_area().add(hbox_main)
        self.show_all()


win = Window_Main()
win.connect('destroy', Gtk.main_quit)
win.show_all()
Gtk.main()