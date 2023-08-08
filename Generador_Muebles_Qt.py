import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QDialog,
    QLabel,
    QPushButton,
    QLineEdit,
    QTextEdit,
    QVBoxLayout,
    QHBoxLayout
)
from PyQt6.QtGui import QDoubleValidator, QPixmap #, QIntValidator

from Interface import Modulo_Util_Qt as Util_Qt
from Modulos import Modulo_Muebles as Muebles
from Modulos.Modulo_Language import get_text as Lang


class Window_Main(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle( Lang('gen_furniture') )
        self.resize(316, 128)
        
        # Contenedor Principal
        vbox_main = QVBoxLayout()
        self.setLayout(vbox_main)
        
        # Opciones - Botones Principales
        button_corner_shelving = QPushButton( Lang('corner_shelving') )
        button_corner_shelving.clicked.connect(self.evt_corner_shelving)
        vbox_main.addWidget( button_corner_shelving )
        
        button_table = QPushButton( Lang('table') )
        button_table.clicked.connect(self.evt_table)
        vbox_main.addWidget( button_table )
        
        # Separador de windgets - Separador de todas las opciones
        vbox_main.addStretch()
        
        # Opcion final - Boton para salir
        button_exit = QPushButton( Lang('exit') )
        button_exit.clicked.connect(self.evt_exit)
        vbox_main.addWidget( button_exit )
        
        # Fin, Mostrar ventana y todo el contenido
        self.show()
    
    def evt_corner_shelving(self):
        self.hide()
        Dialog_Furniture(self, furniture='corner_shelving').exec()
        self.show()
    
    def evt_table(self):
        self.hide()
        Dialog_Furniture(self, furniture='table').exec()
        self.show()
    
    def evt_exit(self):
        self.close()


class Dialog_Furniture(QDialog):
    def __init__(
        self, parent=None, furniture='corner_shelving'
    ):
        super().__init__(parent)
        self.setWindowTitle(Lang(furniture))
        self.resize(256, 128)
        
        self.furniture = furniture
        
        # Contenedor Principal
        vbox_main = QVBoxLayout()
        self.setLayout(vbox_main)
        
        # Seccion Vertical - Grosor
        hbox = QHBoxLayout()
        vbox_main.addLayout(hbox)
        
        label_thickness = QLabel(Lang('thickness'))
        hbox.addWidget(label_thickness)
        
        hbox.addStretch()
        
        self.entry_thickness = QLineEdit(
            placeholderText=Lang('cm')
        )
        self.entry_thickness.setValidator(QDoubleValidator())
        hbox.addWidget(self.entry_thickness)
        
        # Seccion Vertical - Ancho
        hbox = QHBoxLayout()
        vbox_main.addLayout(hbox)
        
        label_width = QLabel(Lang('width'))
        hbox.addWidget(label_width)
        
        hbox.addStretch()
        
        self.entry_width = QLineEdit(
            placeholderText=Lang('cm')
        )
        self.entry_width.setValidator(QDoubleValidator())
        hbox.addWidget(self.entry_width)
        
        # Seccion Vertical - Alto
        hbox = QHBoxLayout()
        vbox_main.addLayout(hbox)
        
        label_height = QLabel(Lang('height'))
        hbox.addWidget(label_height)
        
        hbox.addStretch()
        
        self.entry_height = QLineEdit(
            placeholderText=Lang('cm')
        )
        self.entry_height.setValidator(QDoubleValidator())
        hbox.addWidget(self.entry_height)
        
        # Seccion Vertical - Agregar espaciado
        vbox_main.addStretch()
        
        # Seccion Vertical final - Iniciar - Generar Mueble
        button_get_furniture = QPushButton(Lang('get_furniture'))
        button_get_furniture.clicked.connect(self.evt_get_furniture)
        vbox_main.addWidget(button_get_furniture)
        
        # Fin, Mostrar ventana
        self.show()
    
    def evt_get_furniture(self):
        # Verificar si es cero o no
        if (
            self.entry_thickness.text() == '0' or
            self.entry_width.text() == '0' or
            self.entry_height.text() == '0'
        ):
            # Si es cero, entonces los caracteres seran nulos o ''
            self.entry_thickness.setText('')
            self.entry_width.setText('')
            self.entry_height.setText('')
        else:
            # No es cero, así que esta bien.
            pass
        
        # Si es posible, obtener datos del mueble
        try:
            # Obtencion de datos para armar mueble
            thickness = float(self.entry_thickness.text())
            width = float(self.entry_width.text())
            height = float(self.entry_height.text())
            
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
            else:
                pass
        
        except:
            # Datos erroneos
            text_furniture = 'ERROR'
        
        self.hide()
        Dialog_View_TextImage(
            self,
            text=text_furniture,
            image_from_file=f'./Images/furniture_{self.furniture}.png'
        ).exec()
        self.close()


class Dialog_View_TextImage(QDialog):
    def __init__(
        self, parent=None,
        text=Lang('text'),
        image_from_file=''
    ):
        super().__init__(parent)
        
        self.setWindowTitle(Lang('text&image'))
        self.resize(512, 512)
        
        # Contenedor Principal
        hbox_main = QHBoxLayout()
        self.setLayout(hbox_main)
        
        # Seccion Horizontal 1 - Text Edit
        text = str(text).replace('\n', '<br>')
        text_edit = QTextEdit( text )
        text_edit.setReadOnly(True)
        hbox_main.addWidget(text_edit)
        
        # HBox Separador
        #hbox_main.addStretch()
        
        # Seccion Horizontal 2 - Imagen
        label = QLabel()
        pixmap = QPixmap(image_from_file)
        pixmap = (
            (pixmap.scaledToWidth(256)).scaledToHeight(256)
        )
        label.setPixmap(pixmap)
        hbox_main.addWidget(label)
        
        # HBox Separador - Para poner acomodada la imagen
        #hbox_main.addStretch()
        
        # Fin Mostrar todo lo necesario
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window_Main()
    sys.exit(app.exec())