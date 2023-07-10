import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib

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
        dialog = Dialog_corner_shelving(self)
        dialog.run()
        dialog.destroy()
        self.show_all()
    
    def evt_table(self, widget):
        print()
    
    def evt_exit(self, widget):
        self.destroy()


class Dialog_corner_shelving(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(
            title=Lang('corner_shelving'),
            transient_for=parent, flags=0
        )
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
        self.entry_thickness.set_placeholder_text( Lang('thickness') )
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
        self.entry_width.set_placeholder_text( Lang('width') )
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
        self.entry_height.set_placeholder_text( Lang('height') )
        self.entry_height.connect(
            'changed', self.on_entry_onlyNumber
        )
        hbox.pack_end(self.entry_height, False, True, 0)
        
        # Seccion Vertical Final - Obtener mueble
        self.button_get_furniture = Gtk.Button( label='Obtener mueble' )
        self.button_get_furniture.connect(
            'clicked', self.evt_get_furniture
        )
        vbox_main.pack_end(self.button_get_furniture, False, True, 16)
        
        # Fin, Mostrar ventana y todo
        self.get_content_area().add(vbox_main)
        self.show_all()
    
    def on_entry_onlyNumber(self, entry):
        # Aceptar solo caracteres de tipo numero
        text = entry.get_text().strip()
        entry.set_text(
            ''.join(
                [ i for i in text if i in '0123456789']
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
            
            text_furniture = Muebles.Corner_shelving(
                thickness=thickness,
                width=width,
                height=height
            )
        except:
            # Datos erroneos
            text_furniture = 'ERROR'
        
        self.hide()
        dialog = Util_Gtk.Dialog_TextView(
            self,
            text=text_furniture
        )
        dialog.run()
        dialog.destroy()
        self.destroy()


win = Window_Main()
win.connect('destroy', Gtk.main_quit)
win.show_all()
Gtk.main()